
name = input("Enter your name: ")

#determine length of name string
result = len(name)
print(result)

#find the first occurance of the letter "r" in the name string
result = name.find("r")
print(result)

#find the last occurance of the letter "r" in the name string
result = name.rfind("r")
print(result)

#will return -1 if a letter " " is not found in the name string
result = name.find("q")
print(result)

#capitalize the first letter of a string and make the rest of the string lowercase
result = name.capitalize()
print(result)

#use the Upper method to capitalize all letters in a string
result = name.upper()
print(result)

#use the lower method to make all letters in a string lowercase
result = name.lower()
print(result)

#use isdigit to check if the string is a number and return a boolean value
result = name.isdigit()
print(result)

#use isalpha to check if the string is a letter and return a boolean value
result = name.isalpha()
print(result)

phone_number = input("Enter your phone number: ")
phone_result = phone_number.count("-")
print(phone_result)

#use the replace method to replace a character in a string
#THIS IS ONE OF THE MOST USEFUL METHODS
phone_number = name.replace("-", "")
print(phone_number)

#FOR A COMPREHENSIVE LIST OF STRING METHODS, VISIT: https://www.w3schools.com/python/python_ref_string.asp
#use the help() function to get more information on a method

#print(help(str)) #this will print a list of all string methods