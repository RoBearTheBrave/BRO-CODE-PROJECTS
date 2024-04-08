# In python we can add multiple methods to a class by chaining them together with the dot operator

class Car:

    def turn_on(self):
        print("The car is starting")
        return self # If we return self we can chain methods together otherwise we will get an error

    def drive(self):
        print("The car is driving")
        return self

    def brake(self):
        print("The car is stopping")
        return self

    def turn_off(self):
        print("The car is stopping")
        return self


car = Car()


car.turn_on()
car.drive()
car.brake()
car.turn_off()

# we can use the dot operator to chain methods together
car.turn_on().drive().brake().turn_off() #this can be difficult to read, so you can use /n to make it more readable and break it up onto multiple lines