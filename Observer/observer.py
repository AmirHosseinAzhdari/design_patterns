"""Observer (Behavioral)
        1-Subject, 2-Notify, 3-Observers 

Sending signals to other parts of the project and notifying them of changes made

"""

class One:
    def update(self, subject):
        print(f"One {subject.name} new {subject.data}")


class Two:
    def update(self, subject):
        print(f"Two {subject.name} new {subject.data}")


class Observer:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)
        
    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0
        
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
        
        
d1 = Data("first")
d2 = Data("second")

o = One()
t = Two()

d1.attach(o)
d2.attach(t)

d1.data = 34
d2.data = 87