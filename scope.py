# variable scope is the part of a program where a variable is visible and can be accessed
# scope resolution is the process of determining the value of a variable based on the scope in which it is defined
# scope resolution = (LEGB) Local -> Enclosing -> Global -> Built-in

####################### python will look for a variable in the following order: #######################
# 1. Local scope  - variables defined inside a function
# 2. Enclosing scope - variables defined in an enclosing function
# 3. Global scope - variables defined at the top level of a module
# 4. Built-in scope - variables defined in the built-in namespace
# python will use the first variable it finds in the order above


#-------------------------Local Scope-------------------------
#### these functions cannot access each other's variables because they are in different scopes
def func1():
    x = 10
    print(y)

def func2():
    y = 20
    print(x)

# we can give functions access to variables in other scopes by passing them as arguments

def func3():
    x = 10
    print(x)

def func4():
    x = 20
    print(x)


#-------------------------Enclosing Scope-------------------------
def func5():
    x = 10
    def inner():
        print(x)
    inner()


#-------------------------Global Scope-------------------------
def func6():
    print(x)

def func7():
    print(x)

x = 10 # this is a global variable that can be accessed by any function in the program

func6()
func7()


#-------------------------Built-in Scope-------------------------
def func8():
    print(abs(-10)) # abs is a built-in function from the math module