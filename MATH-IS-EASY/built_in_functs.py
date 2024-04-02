
x = 3.14
y = -4
z = 5

rounding_result = round(x)
abs_result = abs(y)
power_result = pow(y, z) #(base, exponent)
max_result = max(x, y, z)
min_result = min(x, y, z)

print(f"The rounding result is {rounding_result}")
print(f"The absolute value result is {abs_result}")
print(f"The exponential result is {power_result}")
print(f"The max value result is {max_result}")
print(f"The min value result is {min_result}")

#using the math module
import math

a = 9.1

#use the value of pi
print(math.pi)

#use the value of e (from physics exponetial constant)
print(math.e)

#use the square root
sq_result = math.sqrt(a)
print(f"The square root value result is {sq_result}")

#round a number up
b = 9.1
round_up_result = math.ceil(b)
print(f"The rounded up value result is {round_up_result}")

#round a number down
round_down_result = math.floor(b)
print(f"The rounded down value result is {round_down_result}")

##USEFUL MATH FUNCTIONS##
#requires import math

radius = float(input('Enter the radius of a circle: '))
# Circumference == 2*pi*r
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")


#calculate area of circle
# Area == pi * r^2

area = math.pi * pow(radius, 2)
print(f"The area is: {round(area, 2)}cm^2")


#Calculate the hypotenuse(the long side) of a right triangle
# c = square root of (a^2 + b^2)

a_side = float(input("Enter side A: "))
b_side = float(input("Enter side B: "))

c_side = math.sqrt(pow(a_side, 2) + pow(b_side, 2))

print(f"Side C = {c_side}")