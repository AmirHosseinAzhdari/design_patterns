"""Chain Of Responsibility (Behavioral)

For algorithms with varied responses and avoid a large number of conditions

"""

from abc import ABC, abstractclassmethod


class AbstractHandler(ABC):

    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self.proccess_request(request)
        if not handled:
            self._successor.handle(request)

    @abstractclassmethod
    def proccess_request(self, request):
        pass


# ------------------------------------------------------------------------------------------------------   

class HandlerOne(AbstractHandler):
    def proccess_request(self, request):
        if 0 < request <= 10:
            print(f"Handler one is proccessing this request {request}")
            return True


class HandlerTwo(AbstractHandler):
    def proccess_request(self, request):
        if 10 < request <= 20:
            print(f"Handler two is proccessing this request {request}")
            return True


class DefaultHandler(AbstractHandler):
    def proccess_request(self, request):
        print(f"This request has no handler, so default handler proccess this request .. {request}")
        return True


# ------------------------------------------------------------------------------------------------------

class Client:

    def __init__(self):
        # handler two is successor of handler one
        self._handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self._handler.handle(request)


requests = [3, 4, 32, 12, 8, 19]

c = Client()
c.delegate(requests)
