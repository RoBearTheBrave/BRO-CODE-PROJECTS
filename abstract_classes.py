# abstract classes prevent a user from creating an object of the class
# abstract classes are used to define a blueprint for other classes, like a ghost class

# compels a user to override the abstract methods in the child class

# abstract classes are created using the abc module
# when we want to prevent a user from creating an object from a class, we can use the ABC class from the abc module

from abc import ABC, abstractmethod

class Vehicle(ABC):

 
    @abstractmethod # we need to use this decorator to make the method abstract
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("This car is moving")

class Motorcycle(Vehicle):
    def go(self):
        print("This motorcycle is moving")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# if we want to create an object of a car or motorcycle, we can do that, but we need to create it directly from the Car or Motorcycle class