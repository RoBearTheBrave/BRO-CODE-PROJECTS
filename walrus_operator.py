# the walrus operator is a new feature in Python 3.8
# it is represented by the := operator
# it is used to assign a value to a variable as part of a larger expression
# it is useful for reducing code duplication


happy = True
print(happy)
#combine these two lines of code into one line using the walrus operator
# print(happy = True) # this will not work

print(happy := True) # this will work, because the walrus operator is used to assign a value to a variable as part of a larger expression



foods = list()
while True:
    food = input("Enter a food: ")
    if food == "quit":
        break
    foods.append(food)

# to write this same code with the walrus operator, we can combine the while loop with the input statement
foods = list()
while (food := input("Enter a food: ")) != "quit":
    foods.append(food)