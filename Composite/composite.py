"""Composite (Behavior)
    1- leaf: don't have subsets
    2- composite: have subsets

It is used in tree structures, if there is an object that may be a subset of another object and ...

"""

from abc import ABC, abstractclassmethod


class World(ABC):
    @abstractclassmethod
    def show(self): pass


class Being(World):
    def __init__(self, name):
        self.name = name
        self._children = []

    def add(self, object):
        self._children.append(object)

    def remove(self, object):
        self._children.remove(object)

    def show(self):
        print(f"Being composite {self.name}")
        for child in self._children:
            child.show()


class Animal(Being):
    def show(self):
        print(f"\tAnimal composite {self.name}")
        for child in self._children:
            child.show()


class Human(Being):
    def show(self):
        print(f"\tHuman composite {self.name}")
        for child in self._children:
            child.show()


class Cat(Animal):
    def show(self):
        print(f"\t\tCat leaf {self.name}")


class Dog(Animal):
    def show(self):
        print(f"\t\tDog leaf {self.name}")


class Male(Human):
    def show(self):
        print(f"\t\tMale leaf {self.name}")


class Female(Human):
    def show(self):
        print(f"\t\tFemale leaf {self.name}")


cat = Cat('Missy')
dog = Dog('Jack')

male = Male('Mark')
female = Female('Jane')

animal = Animal('Animal')
human = Human('Human')

animal.add(cat)
animal.add(dog)
human.add(male)
human.add(female)

being = Being('Being')

being.add(human)
being.add(animal)

being.show()
