# with POOP - Python Object Oriented Programming - you can create things as your own modules by creating a class in a file with a .py extension
# eg phone, popcorn, car, etc

# we can use programing to mimic real world objects
# we can use ATTRIBUTES (WHAT AN OBJECT IS OR HAS) to define the state of objects
# we can use METHODS to define the behavior/actions (WHAT AN OBJECT CAN DO) of objects

# we can create classes that represent real world objects
# classes are like blueprints that define the properties and behaviors of objects

# classes are defined using the class keyword
# class names are typically capitalized
# class names are usually singular nouns
# classes can have attributes and methods
# small classes can be left inside the main module, but larger classes should be put in their own module
  


# create a car class
class Car: 
    def __init__(self, make, model, year, color): # the __init__ method is a special method that is called when an object is created # self must be the first parameter in all method definitions
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print(f"The {self.make} {self.model} is driving")   

    def stop(self):
        print(f"The {self.make} {self.model} is stopping")  

