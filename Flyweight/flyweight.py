"""Flyweight (Structural)
    1-Context, 2-FlyweightFactory, 3-Flyweight

lets you fit more objects into the available amount of RAM by sharing common parts of state between
 multiple objects instead of keeping all of the data in each object.

"""
import json
from typing import Dict, List


class Flyweight:
    def __init__(self, shared_state: List):
        self._shared_state = shared_state

    def operation(self, unique_state: List):
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: List):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: List):
        return "_".join(sorted(state))

    def get_or_create_flyweight(self, shared_state: List):
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_cars(factory: FlyweightFactory, plates: str, owner: str, brand: str, model: str, color: str):
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_or_create_flyweight([brand, model, color])
    flyweight.operation([plates, owner])


factory = FlyweightFactory([
    ["Chevrolet", "Camaro2018", "pink"],
    ["Mercedes Benz", "C300", "black"],
    ["Mercedes Benz", "C500", "red"],
    ["BMW", "M5", "red"],
    ["BMW", "X6", "white"],
])

factory.list_flyweights()

add_cars(factory, "CL234IR", "James Doe", "BMW", "M5", "red")

add_cars(factory, "CL234IR", "James Doe", "BMW", "X1", "red")

print("\n")

factory.list_flyweights()