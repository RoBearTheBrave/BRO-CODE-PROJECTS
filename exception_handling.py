# exception = an event that occurs during the execution of a program that disrupts the normal flow of instructions


# use the try / except block to handle exceptions when you suspect an error may occur in your code

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    #print(result) -- add in exception handling to catch errors before the result is printed
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero")
except ValueError as e:
    print(e)
    print("Invalid input. Numbers only please")
except Exception as e: # this will catch ANY exception that occurs, so it's best to use this as the last exception
    print(e)
    print("Something went wrong, but we don't know what it is")
else:
    print(result)
finally:
    print("This will always execute") # this is a good place to put clean-up code like closing files or database connections