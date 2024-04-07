# arbitrary or variable-length arguments are used when we do not know how many arguments will be passed to a function
# this allows us to pass any number of arguments to a function

# use *args to pass a variable number of arguments to a function inside of a tuple
# use **kwargs to pass a variable number of keyword arguments to a function inside of a dictionary

def add(*args): #you can change the name or args to anything you want, but you must use the * symbol (the unpacking operator) before the name
    total = 0
    for arg in args:
        total += arg
    return total

#print(add(1, 2, 3, 4, 5)) # 15

# def display_name(*args):
#     for name in args:
#         print(args, end=" ")    

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III") 


#using **kwargs to pass a variable number of keyword arguments to a function

# def print_address(**kwargs): #you can change the name of kwargs to anything you want, but you must use the ** symbol before the name
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Main St", city="Springfield", state="IL", zip="62701")

def shipping_label(*args, **kwargs):
    for name in args:
        print(name, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}") #get is a method that returns the value of the specified key
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III", 
                     street="123 Main St", 
                     #apt="Apt 1",
                     pobox="PO Box 123",
                     city="Springfield", 
                     state="IL", 
                     zip="62701")