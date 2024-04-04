#use 2D collections to create a keypad for a phone

#these numbers need to be in order, so we should use a tuple

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end = " ") #end = " " will print the numbers on the same line with a space between them
    print() #this will print a new line after each row of numbers