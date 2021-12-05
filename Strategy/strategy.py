"""Strategy (Behavior)

A class with various algorithms that can be used by any of them at runtime

"""

from abc import ABC, abstractclassmethod


class Direction(ABC):
    
    @abstractclassmethod
    def direct(self, data):
        pass
    

class Right(Direction):
    
    def direct(self, data):
        print(data[::-1])
        

class Left(Direction):
    
    def direct(self, data):
        print(data)


class Context:
    
    def __init__(self, direction, sentence):
        self._direction = direction
        self._sentence = sentence
        
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, dir):
        self._direction = dir
        
    def sorting(self):
        return self._direction.direct(self._sentence)
    

c1 = Context(Right(), "Hello world")
c1.sorting()