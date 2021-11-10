"""
    Creational:
        Singleton
"""

# python uses singleton for multiple imports.
import math as m1
import math as m2
# same id for 2 same import.
print(id(m1))
print(id(m2))

# Singleton class
class Singleton(type):
    _instance = None
    
    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwds)
        return self._instance
    
class Db(metaclass=Singleton):
    pass

# create 2 instance of Db class
d1 = Db()
d2 = Db()

# same id for multi instances of a class
print(id(d1))
print(id(d2))