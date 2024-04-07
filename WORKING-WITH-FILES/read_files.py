# read the contents of a file and print it to the console


path = "/Users/robertthibault/Projects/BRO-CODE/BRO-CODE-PROJECTS/test_file.txt"


# incase the file doesn't exist we can use a try except block to handle the error
try:
    with open(path) as file: #using with open with automatically close the file when the block of code is done
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file could not be found")


#print(file.closed) # this test will return True because the file is closed