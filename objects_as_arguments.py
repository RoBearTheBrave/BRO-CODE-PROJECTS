# how to pass an object as an argument to a function
# the type of attributes that an object might have can be limited to the attributes that are defined in the class

class Car: 

    color = None

def change_color(car, color): #argument names should be lowercase
    car.color = color



#create some car objects
my_car = Car()
my_truck = Car()
my_bike = Car()

change_color(my_car, "red")
change_color(my_truck, "blue")
change_color(my_bike, "green")



print(my_car.color)
print(my_truck.color)
print(my_bike.color)