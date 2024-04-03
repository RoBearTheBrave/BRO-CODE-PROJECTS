# nested loops are loops within loops
# they can be useful when you need to loop over a sequence of sequences


for i in range(3):
    for x in range(1,11,1):
        print(x, end="") # use the end parameter with an empty string to print on the same line. input any other character to separate the numbers
    print()


#print a rectangle of symbols based on user inputs
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol you want to use: ")

for a in range(rows):
    for b in range(columns):
        print(symbol, end="")
    print()
 