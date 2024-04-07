#this can move files, but it can move folders too -- be careful

import os

source = "move_test_file.txt"
destination = "/Users/robertthibault/Desktop/test/move_test_file.txt"

try:
    if os.path.exists(destination):
        print("There is already a file at the destination")
    else:
        os.replace(source, destination)
        print(source + " was moved to " + destination)
except FileNotFoundError as e:
    print(e)
    print(source + " could not be found")