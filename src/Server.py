from datetime import date
from threading import Thread

import DiagChamber
import Error
from Database import Database
from Request import Request as Rq
from Request import translate
from Error import Error as Err
from BlockingQueue import BlockingQueue


class Server:

    def __init__(self):
        self.requests = BlockingQueue()
        self.database = Database()
        self.heads = []
        self.running = False

    def process(self, data):
        rq = input().split()
        data.append(rq)
        self.heads.append(translate.get(rq[0], Rq.UNRECOGNIZED))
        if translate.get(rq[0], Rq.UNRECOGNIZED) != Rq.DISCONNECT:
            return True
        else:
            self.running = False
            return False

    def run(self):
        self.running = True
        data = []

        while self.process(data):
            request = data.pop()
            err = Err.ERR_NONE
            head = translate.get(request[0], Rq.UNRECOGNIZED)
            request = request[1::]
            match head:
                case Rq.REGISTER:
                    head = request[0]
                    request = request[1::]
                    self.database.register_component(head, request)
                case Rq.LAUNCH_DIAGNOSTIC:
                    self.database.get("-dc", int(request[0])).start_diagnostic()
                case Rq.LOAD_BATTERIES:
                    dc = self.database.get("-dc", 0)
                    batteries = [(self.database.get("-b", int(a)), b) for (a, b) in zip(*[iter(request[1::])] * 2)]
                    for (battery, channel) in batteries:
                        dc.load_battery(battery, channel)
                case Rq.ABORT_DIAGNOSTIC:
                    err = self.database.get(request[0], None).unload(True)
                case Rq.SAVE:
                    self.database.save()
                case Rq.LOAD:
                    self.database.load()
                case Rq.TO_STRING:
                    self.database.toString()
                case Rq.POP:
                    self.database.remove(request[0], request[1])
                case Rq.ADVANCE_TIME:
                    self.database.get("-dc", int(request[0])).advance_time(int(request[1]))
                case Rq.GENERATE_FILE:
                    dc = self.database.get("-dc", int(request[0]))
                    for (channel, battery) in dc.loaded_batteries.items():
                        print("Channel {}:{} ------ {}".format(channel, battery.generateProtocol(),
                                                               battery.generateFile()))
                case Rq.DIAG:
                    num = 0
                    for (name, tc) in self.database.tempChambers.items():
                        batteries = tc.check_diag()
                        if len(batteries) > 0:
                            num += 1
                            print("{}:".format(name))
                            for barcode in batteries:
                                print(barcode)
                    if num == 0:
                        print("No cells need to undergo diagnostic")
                case Rq.STATUS:
                    num = int(request[0])
                    dc = self.database.get("-dc", num)
                    days = (dc.finish_date - date.today())
                    days = dc.time.days - days.days
                    time = dc.time.days
                    if days < time:
                        print("{}/{} days".format(days, time))
                    else:
                        print("Diagnostic is complete please check diagnostic chamber to verify completion")
                case Rq.UNLOAD:
                    dc = self.database.get("-dc", int(request[0]))
                    dc.unload()
                case Rq.DISCONNECT:
                    print("Disconnected")
                    break
                case other:
                    print("Illegal request")

        self.database.save()

    def receive_request(self, request):
        """
        This method will add the request to the requests

        Parameter
        ---------
        :param request: Request
            The request we want to add to the requests
        """
        self.requests.enqueue(request)

    def isRunning(self):
        return self.running

