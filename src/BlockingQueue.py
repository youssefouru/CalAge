import threading
import collections


class BlockingQueue(object):
    def __init__(self):
        self.pulling = threading.Semaphore(0)
        self.queue = collections.deque()
        self.size = 0

    def isEmpty(self):
        """

        :return:
        """
        return self.size == 0

    def enqueue(self, elem):
        """
        This is used to an element into the blocking queue.

        Parameter
        ---------
        :param elem: T
            The elem we want to add
        """
        self.queue.append(elem)
        self.pulling.release()
        self.size += 1

    def dequeue(self):
        self.pulling.acquire()
        self.size -= 1
        return self.queue.pop()
