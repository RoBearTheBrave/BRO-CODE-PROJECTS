# logical operators are used to combine conditional statements

#           and operator (and) checks if two or more conditions are true
#           or operator (or) checks if one or more conditions are true
#           not operator (not) checks if a condition is false




# Example and operator
# and operator is GOOD FOR CHECKING IF SOMETHING IS WITHIN A RANGE
temp = 25

#if both conditions are true, the output will be "The temperature is ideal"
#if one of these conditions is false, the output will be "The temperature is not ideal"
if temp > 20 and temp < 30:
    print("The temperature is ideal")
else:
    print("The temperature is not ideal")

# Example or operator
# or operator is GOOD FOR CHECKING IF SOMETHING IS OUTSIDE A RANGE
# only one of the conditions needs to be true for the output to be "The temperature is ideal"
sunny = True

if temp <= 20 or temp >= 30:
    print("The temperature is ideal")
else:
    print("The temperature is not ideal")
# Example not operator
    # not operator is GOOD FOR CHECKING IF A CONDITION IS FALSE
if not sunny:
    print("The sun is shining")
else:
    print("The sun is not shining")
