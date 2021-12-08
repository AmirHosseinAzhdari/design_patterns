"""Bridge (Structural)

divides business logic or huge class into separate class hierarchies that can be developed independently.

"""

from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Here's the result on the platform B."


class Abstraction:
    def __init__(self, implementation: Implementation):
        self._implementation = implementation

    def operation(self):
        return f"Abstraction: Base operation with : \n {self._implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    def operation(self):
        return f"Extended Abstraction: Extended operation with: \n {self._implementation.operation_implementation()}"


def client(abstraction: Abstraction):
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client(abstraction)
