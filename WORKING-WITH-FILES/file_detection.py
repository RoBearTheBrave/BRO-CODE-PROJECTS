# how to do basic things with files

import os

#check if a file exists someplace on your computer
path = "/Users/robertthibault/Desktop/test/"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That location is a file")
    elif os.path.isdir(path):
        print("That location is a directory")
else:
    print("That location does not exist") 
