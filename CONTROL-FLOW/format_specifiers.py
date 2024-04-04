# format specifiers are used to format strings in python
# use {:flags} to FORMAT F STRINGS  based on the flags you want to use

# :(number)f - this will format the number to a float with the number of decimal places you specify
# :(number) - this will format the number to a string with the number of characters you specify
# :03 - this will format the number to a string with 3 characters
# :03d - this will format the number to an integer with 3 characters
# :03f - this will format the number to a float with 3 characters
# :.2f - this will format the number to a float with 2 decimal places
# :.2% - this will format the number to a percentage with 2 decimal places

# :< - this will left align the string
# :> - this will right align the string
# :^ - this will center the string

# :+ - this will display the number with a + sign
# :- - this will display the number with a - sign
# : - this will display the number with a space
# :, - this will display the number with a comma


price1 = 50000
price2 = -10000
price3 = 15325.50

print(f"Price 1: ${price1:<,.1f}")
print(f"Price 2: ${price2:^.3f}")
print(f"Price 3: ${price3:>,.2f}")