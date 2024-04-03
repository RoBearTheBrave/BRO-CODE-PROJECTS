#valid credit card numbers using python

# 1. Remove all "-" and ' ' from the credit card number
# 2. Add all digits in the odd places from right to left
# 3. Double every second didgit from right to left
#      (If result is a two digit number, add the digits together)
# 4. Sum the totals from steps 2 and 3
# 5. If the result is divisible by 10, the credit card number is valid

# Step 1
credit_card_number = input("Enter your credit card number: ")
credit_card_number = credit_card_number.replace("-", "").replace(" ", "")
credit_card_number = credit_card_number[::-1] #reverse the credit card number

# Step 2
sum_odd_digits = 0
for x in credit_card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
sum_even_digits = 0
for x in credit_card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
    print("This is a valid credit card number")
else:
    print("This is not a valid credit card number")