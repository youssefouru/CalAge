from Request import Request as Rq
from Request import translate
from BlockingQueue import BlockingQueue
import itertools


class Server:

    def __init__(self, shutdown=[]):
        self.requests = BlockingQueue()
        self.batteries = {}
        self.tempChamber = {}
        self.diagChamber = {}
        self.heads = []
        self.shutdown = shutdown

    def run(self):
        self.shutdown.append(0)
        request = self.requests.dequeue()
        head = translate[request[0]]
        self.heads.append(head)
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
            head = translate[request[0]]
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
