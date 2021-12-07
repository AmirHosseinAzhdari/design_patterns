""" Prototype (Creational)

copy of an object

"""

from copy import deepcopy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:
    """ sample of prototype copy
    """

    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        clone_obj = deepcopy(self._objects.get(name))
        clone_obj.__dict__.update(kwargs)
        return clone_obj


# instance of persons class
p1 = Person("amir", 32)

# make new instance of our copy
pro1 = Prototype()
pro1.register('person1', p1)

person_copy = pro1.clone('person1')

# print copy details
print(person_copy.__dict__)

# same ids
print(id(person_copy.name))
print(id(p1.name))

# change data of copy instance
person_copy = pro1.clone("person1", age=21)
print(person_copy.__dict__["age"])
