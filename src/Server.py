from Request import Request as Rq
from BlockingQueue import BlockingQueue
import itertools


class Server:

    def __init__(self):
        self.requests = BlockingQueue()
        self.batteries = {}
        self.tempChamber = {}
        self.diagChamber = {}
        self.running = itertools.count()

    def run(self):
        self.running = next(self.running)
        request = self.requests.dequeue()
        head = request[0]
        while head is not Rq.DISCONNECT:
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
            request = self.requests.dequeue()
            head = request[0]
        self.running = next(self.running)

    def receive_request(self, request):
        """
        This method will add the request to the requests

        Parameter
        ---------
        :param request: Request
            The request we want to add to the requests
        """
        self.requests.enqueue(request)
