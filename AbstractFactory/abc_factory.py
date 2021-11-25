""" Abstract Factory

Car => Benz, Bmw => Suv, Coupe
    benz suv -> gla, glc
    bmw suv -> x1, x2
    
    benz coupe -> cls, E-class
    bmw coupe -> m2, m4

"""

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass
    
    @abstractmethod
    def call_coupe(self):
        pass
    
# ------------------------------------------------

class Benz(Car):
    def call_suv(model):
        return model
    
    def call_coupe(model):
        return model
    
class Bmw(Car):
    def call_suv(model):
        return model
    
    def call_coupe(model):
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

class Gla(Suv):
    def creating_suv(self):
        print("This is yuor suv benz gla ...")
        
class Glc(Suv):
    def creating_suv(self):
        print("This is yuor suv benz glc ...")
        
class X1(Suv):
    def creating_suv(self):
        print("This is yuor suv bmw x1 ...")
        
class X2(Suv):
    def creating_suv(self):
        print("This is yuor suv bmw x2 ...")
        
# ------------------------------------------------

class Cls(Coupe):
    def creating_coupe(self):
        print("This is yuor coupe benz cls ...")
        
class Eclass(Coupe):
    def creating_coupe(self):
        print("This is yuor coupe benz e-class ...")
        
class M2(Coupe):
    def creating_coupe(self):
        print("This is yuor coupe bmw m2 ...")
        
class M4(Coupe):
    def creating_coupe(self):
        print("This is yuor coupe bmw m4 ...")
        
# ------------------------------------------------

def client_suv(corp, model):
    suv = corp().call_suv(model())
    suv.creating_suv()
    
def client_coupe(corp, model):
    coupe = corp().call_suv(model())
    coupe.creating_coupe()
    
# ------------------------------------------------

client_coupe(Bmw())
client_coupe(Benz())
client_suv(Bmw())
client_suv(Benz())