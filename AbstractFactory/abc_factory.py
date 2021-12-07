""" Abstract Factory (Structural)

Car => Benz, Bmw => Suv, Coupe
    benz suv -> gla, glc
    bmw suv -> x1, x2
    
    benz coupe -> cls, E-class
    bmw coupe -> m2, m4

"""

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def call_suv(self, model):
        pass

    @abstractmethod
    def call_coupe(self, model):
        pass


# ------------------------------------------------

class Benz(Car):
    def call_suv(self, model):
        return model

    def call_coupe(self, model):
        return model


class Bmw(Car):
    def call_suv(self, model):
        return model

    def call_coupe(self, model):
        return model


# ------------------------------------------------

class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass


# ------------------------------------------------

class Gla(Suv, Benz):
    def creating_suv(self):
        print("This is your suv benz gla ...")


class Glc(Suv, Benz):
    def creating_suv(self):
        print("This is your suv benz glc ...")


class X1(Suv, Bmw):
    def creating_suv(self):
        print("This is your suv bmw x1 ...")


class X2(Suv, Bmw):
    def creating_suv(self):
        print("This is your suv bmw x2 ...")


# ------------------------------------------------

class Cls(Coupe, Benz):
    def creating_coupe(self):
        print("This is your coupe benz cls ...")


class Eclass(Coupe, Benz):
    def creating_coupe(self):
        print("This is your coupe benz e-class ...")


class M2(Coupe, Bmw):
    def creating_coupe(self):
        print("This is your coupe bmw m2 ...")


class M4(Coupe, Bmw):
    def creating_coupe(self):
        print("This is your coupe bmw m4 ...")


# ------------------------------------------------

def order_suv(corp, model):  # corp is company and model is the model of car
    if issubclass(model, corp):
        suv = corp().call_suv(model())
        suv.creating_suv()
    else:
        raise NameError()


def order_coupe(corp, model):
    if issubclass(model, corp):
        coupe = corp().call_coupe(model())
        coupe.creating_coupe()
    else:
        raise NameError()


# ------------------------------------------------

order_coupe(Benz, Eclass)  # This is your coupe benz e-class ...
order_suv(Bmw, X2)  # This is your coupe benz e-class ...
order_suv(Bmw, M2)  # Error
