# A keyword argument is an argument that is preceded by an identifier (e.g. name=) in a function call. The order of keyword arguments does not matter. This allows you to provide values for only the parameters you want to provide values for.

def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

#these are positional arguments, so if they were out of order they would be incorrect
hello("Hello", "John", "Mr.", "Doe")

#these are keyword arguments, so the order does not matter
hello(title="Mr.", first_name="John", last_name="Doe", greeting="Hello")



#print number 1-10 using a for loop
for i in range(1, 11):
    print(i, end=" ") #end=" " is a keyword argument that changes the default value of the end parameter in the print function
    # the built-in print function has a default value for the end parameter of "\n" which is a newline character

#create function that generates a phone number 

def get_phone_number(country_code, area_code, exchange, number):
    return f"+{country_code} ({area_code}) {exchange}-{number}"

get_phone_number = get_phone_number(1, 555, 123, 4567)
print(get_phone_number) # +1 (555) 123-4567