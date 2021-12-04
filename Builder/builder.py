""" Builder (creational)

We have a product that are made from small parts

"""

class Wheel:
    size = None
    
class Body:
    shape = None
    
class Engine:
    hp = None
    
# ------------------------------------------

class Builder:
    def get_engine(self):
        pass

    def get_wheel(self):
        pass
    
    def get_body(self):
        pass

# ------------------------------------------

class Car:
    def __init__(self) -> None:
        self.__wheel = None
        self.__engine = None
        self.__body = None
        
    def set_wheel(self, wheel):
        self.__wheel = wheel
        
    def set_engine(self, engine):
        self.__engine = engine
        
    def set_body(self, body):
        self.__body = body
        
    def detail(self):
        print(f"Body : {self.__body.shape}")
        print(f"Wheel : {self.__wheel.size}")
        print(f"Engine : {self.__engine.hp}")

# ------------------------------------------
    
class Director:
    __builder = None
    
    def set_builder(self, builder):
        self.__builder = builder
        
        
    def get_car(self):
        car = Car()
        
        body = self.__builder.get_body()
        wheel = self.__builder.get_wheel()
        engine = self.__builder.get_engine()
        
        car.set_body(body)
        car.set_engine(engine)
        car.set_wheel(wheel)
        
        return car
    
# ------------------------------------------

class Benz(Builder):
    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel
    
    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body
    
    
class BMW(Builder):
    def get_engine(self):
        engine = Engine()
        engine.hp = 380
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 23
        return wheel
    
    def get_body(self):
        body = Body()
        body.shape = "Sedan"
        return body
    
# ------------------------------------------

car1 = Benz()
director = Director()
director.set_builder(car1)
b1 = director.get_car()
b1.detail()