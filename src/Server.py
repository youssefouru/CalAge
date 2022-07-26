from threading import Thread

from Database import Database
from Request import Request as Rq
from Request import translate
from BlockingQueue import BlockingQueue


class Server:

    def __init__(self, shutdown):
        self.requests = BlockingQueue()
        self.database = Database()
        self.heads = []
        self.shutdown = shutdown

    def process(self, data):
        rq = self.requests.dequeue()
        data.append(rq)
        self.heads.append(rq[0])
        if translate.get(rq[0], Rq.UNRECOGNIZED) != Rq.DISCONNECT:
            return True
        else:
            self.shutdown.pop()
            return False

    def run(self):
        self.shutdown.append(0)
        data = []
        while self.process(data):
            request = data.pop()
            head = translate.get(request[0], Rq.UNRECOGNIZED)
            if head == Rq.REGISTER_BATTERY:
                self.database.register_component("-b", request[1::])
            elif head == Rq.REGISTER_DIAGNOSTIC_CHAMBER:
                self.database.register_component("-dc", request[1::])
            elif head == Rq.REGISTER_TEMPERATURE_CHAMBER:
                self.database.register_component("-tc", request[1::])
            elif head == Rq.LAUNCH_DIAGNOSTIC:
                self.database.get(request[1], None).start_diagnostic()
            elif head == Rq.LOAD_BATTERIES:
                ...
            elif head == Rq.ABORT_DIAGNOSTIC:
                ...
            elif head == Rq.DISCONNECT:
                print("Disconnected")
                break
            else:
                print("Illegal request")


    def receive_request(self, request):
        """
        This method will add the request to the requests

        Parameter
        ---------
        :param request: Request
            The request we want to add to the requests
        """
        self.requests.enqueue(request)


tab = []
server = Server(tab)
server_thread = Thread(target=server.run)
server_thread.start()
while len(tab) > 0:
    print("write")
    request = input().split()
    server.receive_request(request)
print(server.heads)
server_thread.join()
