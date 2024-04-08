# An object will use a method that is more close to it than the one in the parent class


class Animal:

    def eat(self):
        return "This animal is eating"
    
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot") 
    
rabbit = Rabbit()
rabbit.eat() # This rabbit is eating