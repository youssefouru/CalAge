from threading import Thread

from Database import Database
from Request import Request as Rq
from Request import translate
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
        self.heads.append(rq[0])
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
            head = translate.get(request[0], Rq.UNRECOGNIZED)
            if head == Rq.REGISTER_BATTERY:
                self.database.register_component(head, request[1::])
            elif head == Rq.REGISTER_DIAGNOSTIC_CHAMBER:
                self.database.register_component(head, request[1::])
            elif head == Rq.REGISTER_TEMPERATURE_CHAMBER:
                self.database.register_component(head, request[1::])
            elif head == Rq.LAUNCH_DIAGNOSTIC:
                self.database.get(request[1], None).start_diagnostic()
            elif head == Rq.LOAD_BATTERIES:
                dc = self.database.get(request[1], None)
                for i in request[1::]:
                    dc.load(self.database.get("-b", int(i)))
            elif head == Rq.ABORT_DIAGNOSTIC:
                self.database.get(request[1], None).unload(True)
            elif head == Rq.SAVE:
                self.database.save()
            elif head == Rq.LOAD:
                self.database.load()
            elif head == Rq.DISCONNECT:
                print("Disconnected")
                break
            else:
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



