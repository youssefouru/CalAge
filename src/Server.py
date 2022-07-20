from Database import Database
from Request import Request as Rq
from Request import translate
from BlockingQueue import BlockingQueue


class Server:

    def __init__(self, shutdown):
        self.requests = BlockingQueue()
        database = Database()
        self.heads = []
        self.shutdown = shutdown

    def run(self):
        self.shutdown.append(0)
        running = True
        head = Rq.UNRECOGNIZED
        while running:
            if head == Rq.REGISTER_BATTERY:
                ...
            elif head == Rq.REGISTER_DIAGNOSTIC_CHAMBER:
                ...
            elif head == Rq.REGISTER_TEMPERATURE_CHAMBER:
                ...
            elif head == Rq.LAUNCH_DIAGNOSTIC:
                ...
            elif head == Rq.LOAD_BATTERIES:
                ...
            elif head == Rq.ABORT_DIAGNOSTIC:
                ...
            elif head == Rq.DISCONNECT:
                running = False
                print("Disconnected")
                break
            if head != Rq.DISCONNECT:
                request = self.requests.dequeue()
                head = translate.get(request[0], Rq.UNRECOGNIZED)
        self.shutdown.pop()

    def receive_request(self, request):
        """
        This method will add the request to the requests

        Parameter
        ---------
        :param request: Request
            The request we want to add to the requests
        """
        self.requests.enqueue(request)
