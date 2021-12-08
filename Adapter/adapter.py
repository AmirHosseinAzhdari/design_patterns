"""Adapter (Structural)
    1- Adaptee, 2-Adapter, 3-Client
    
When we want to connect two unrelated classes use adapter pattern

"""


class IranSocket:
    _type = '2'


class Adapter:
    _socket = None
    _pin_type = '3To2'

    def __init__(self, socket):
        self._socket = socket


class Fridge:
    _adapter = None
    _pin_type = '3'

    def __init__(self, adapter) -> None:
        self._adapter = adapter

    def freeze(self):
        if self._adapter._pin_type == (self._pin_type + 'To' + self._adapter._socket._type):
            print("Done ..")
        else:
            print("Not usable ..")


i = IranSocket()
adapter = Adapter(i)
f = Fridge(adapter)
f.freeze()
