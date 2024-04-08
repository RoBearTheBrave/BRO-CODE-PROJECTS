# Higher Order Functions do 1 of 2 things:
# 1. take a function as an argument
# 2. return a function

# Example 1: take a function as an argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# Example 2: return a function
def divsisor(n):
    def dividend(x):
        return x / n
    return dividend

# to access the dividend function, we need to call the divisor function
divide_by_2 = divsisor(2)
print(divide_by_2(10)) # 5.0