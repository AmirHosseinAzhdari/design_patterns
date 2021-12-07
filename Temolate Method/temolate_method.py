"""Temolate Method (Behavior)

When we use duplicate code in several places in the program

"""

from abc import ABC, abstractclassmethod


class Top(ABC):
    def template_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.fourth_require()
        self.hook()

    def first_common(self):
        print("I am first common")

    def second_common(self):
        print("I am second common")

    @abstractclassmethod
    def third_require(self):
        pass

    @abstractclassmethod
    def fourth_require(self):
        pass

    def hook(self):
        pass


class One(Top):
    def third_require(self):
        print("I am third require from one ...")

    def fourth_require(self):
        print("I am fourth require from one ...")

    def hook(self):
        print("I am hook from one ...")


class Two(Top):
    def third_require(self):
        print("I am third require from two ...")

    def fourth_require(self):
        print("I am fourth require from two ...")


def client(class_):
    class_.template_method()


client(One())
