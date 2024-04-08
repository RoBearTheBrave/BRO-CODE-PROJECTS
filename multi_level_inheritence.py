# muti-level inheritence is when a class inherits from a class that inherits from another class
# This is like a family tree where a child inherits from a parent who also inherits from their parent

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)
print(dog.eat())
print(dog.bark())


# multiple inheritence is when a class inherits from more than one class

class Prey:
    def flee(self):
        print("This prey is fleeing")  

class Predator:
    def hunt(self):
        print("This predator is hunting")


class Rabbit(Prey):
    def run(self):
        print("This rabbit is running")

class Hawk(Predator):
    def fly(self):
        print("This hawk is flying")

class Fish(Prey, Predator):
    def swim(self):
        print("This fish is swimming")


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()