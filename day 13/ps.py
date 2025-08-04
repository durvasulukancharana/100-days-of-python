from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def wheels(self,no_of_wheels):
        pass
# from abstract import vehicle
class car(vehicle):
    def start(self):
        print("car start with key")
    def wheels(self,no_of_wheels):
        print(no_of_wheels)

class bike(vehicle):
    def start(self):
        print("bike start with key")
    def wheels(self,no_of_wheels):
        print(no_of_wheels)

class aeroplane(vehicle):
    def start(self):
        print("aeroplane start with switch")
    def wheels(self,no_of_wheels):
        print(no_of_wheels)
# from h import car,bike,aeroplane
obj=car()
obj.start()
obj.wheels(4)

obj=bike()
obj.start()
obj.wheels(2)

obj=aeroplane()
obj.start()
obj.wheels(6)

