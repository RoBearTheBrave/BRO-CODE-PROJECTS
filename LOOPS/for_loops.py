# for loops are useful when you know how many times you need to loop
# they execute a block of code a specified number of times
# you can iterate over a sequence (list, tuple, string, range, dictionary, set, etc.)

#better than while loops when you need to do something a fixed number of times

# for counter in range(1, 11):
#     print(counter)
# print("Loop finished")

# for counter in reversed(range(1, 11)):
#     print(counter)
# print("Loop finished")

# for counter in range(1, 11, 2):
#     print(counter)
# print("Loop finished")


credit_card_number = "1234-5678-9012-3456"

# loop over the credit card number, or the length of any variable in steps of 5
#for each pass through the loop, print the next 5 characters
for i in range(0, len(credit_card_number), 5):
    print(credit_card_number[i:i+5])


for x in range(1, 21):
    if x == 13:
        continue #this will skip the print function at 13 in the loop and go to the next iteration
    else:
        print(x)