# Inheritance is a way to form new classes using classes that have already been defined.
# The newly formed classes are called derived (CHILD) classes, the classes that we derive from are called base (PARENT) classes.
# Inheritance is useful because it allows us to create classes that are built upon existing classes, to reuse code and establish a hierarchy for classes.
# By using inheritance, we can make changes to the base class and have those changes automatically implemented in the derived classes.

class Animal: 

    alive = True

    def eat(self):
        return "This animal is eating"
    
    def sleep(self):
        return "This animal is sleeping"
    

class Rabbit(Animal):
    def run(self):
        return "This rabbit is running"

class Fish(Animal):
    def swim(self):
        return "This fish is swimming"

class Hawk(Animal):
    def fly(self):
        return "This hawk is flying"

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# print(fish.eat())
# print(hawk.sleep())


print(rabbit.run())
print(fish.swim())
print(hawk.fly())