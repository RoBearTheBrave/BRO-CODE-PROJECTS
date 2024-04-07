# a function is  block of that is reusable
# a function is defined using the def keyword
# a function can take parameters
# a function can return a value


#use arguments to pass values to a function when you call it, but the function needs to have matching parameters to receive the values
#use parameters to receive values in a function definition
#arguments are the values you pass to a function
#parameters are the values that are received in a function definition

#we can include as many parameters as we want in a function definition
def happy_birthday(name, age):
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old")
    print("Happy Birthday dear " + name)
    print("Happy Birthday to you")
    print("")


happy_birthday("Alice", 60)
happy_birthday("Bob", 39)
happy_birthday("Charlie", 40)



#create a funtion to display an invoice
#3 praameters: name, amount, due_date

def display_invoice(name, amount, due_date):
    print(f"Hello {name}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")

display_invoice("Alice", 100, "2021-01-01")



#return a value from a function
#return is a statement that is used to end a funtion and return a value to the caller

def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def divide(a, b): 
    c = a / b
    return c

print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))



# create a function that returns a full name
def full_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

fulll_name = full_name("alice", "smith")
print(fulll_name)

fulll_name = full_name("bob", "jones")
print(fulll_name)
