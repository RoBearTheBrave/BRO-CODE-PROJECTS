from object_oriented_programming import Car

# create a car object

my_truck = Car("Nissan", "720", 1984, "Orange")

print(my_truck.make)
print(my_truck.model)
print(my_truck.year)
print(my_truck.color)

my_car = Car("Honda", "Element", 2003, "Orange")

print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_car.color)

my_car.drive()
my_car.stop()
my_truck.drive()