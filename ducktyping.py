# ducktyping is the concept where the class of an object is less important than the methods that the object defines.
# the class type is not checked if the object has the minimum required methods


class Duck: 
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("This person caught the critter")


#create an object from each of these classes

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

# with ducktyping we can pass in a different object that has the same methods as the duck object

person.catch(chicken) # This chicken is walking