# while loops are useful when you don't know how many times you need to loop
# The while loop will continue to run until the condition is false

# Example
name = input("Enter your name: ")

while name == "":
    print("Please enter your name")
    name = input("Enter your name: ") #this will give the user a chance to enter their name and stop an infinite loop
print(f"Hello, {name}")


# Example
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

# Example of a program that runs an infinite loop until the user enters 'q'
food = input("Enter your favorite food: ")

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food you like! (q to quit): ")

print("Goodbye")




# adding conditions to the while loop

# Example
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not between 1 and 10")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Great! {num} is between 1 and 10")