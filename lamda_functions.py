# lamda functions = functions written in one line using the lambda keyword
# they accept any number of arguments, but only have one expression (think of it like a shortcut for writing functions)
# they are useful for writing small, throwaway functions


#syntax
# lambda arguments: expression

def double(x):
    return x * 2

print(double(5))

#lambda equivalent
double = lambda x: x * 2
print(double(5))


multiply = lambda x, y: x * y
print(multiply(5, 2)) # need to pass in two arguments because the lambda function has two parameters

add = lambda x, y, z: x + y + z
print(add(5, 2, 30))

full_name = lambda first, last: f"{first} {last}"
print(full_name("Alice", "Smith"))

age_check = lambda age: True if age >= 21 else False
print(age_check(22))