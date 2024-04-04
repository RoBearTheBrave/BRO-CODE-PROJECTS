# indexing = accessing elements of a sequence using [] (indexing operator)
#   [start:stop:step] - slicing operator

# Example of indexing
credit_card_number = "1234-5678-9012-3456"
print(credit_card_number[0]) #prints the first element of the string
print(credit_card_number[1:4]) #prints the second, third, and fourth elements of the string

#pull the last four digits of the credit card number
print(credit_card_number[-4:]) 

#pull the first four digits of the credit card number
print(credit_card_number[:4]) 

#using the step in indexing 
print(credit_card_number[::2]) #prints every other digit of the credit card number

last_digits = credit_card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#to reverse a string using indexing set the step to -1
print(credit_card_number[::-1]) #prints the credit card number in reverse