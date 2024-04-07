import os


path = "copy_test_file.txt"

try:
    os.remove(path)
    #os.rmdir(path) # this will remove a directory
    #shutil.rmtree(path # USE WITH CAUTION this will remove a directory and all of its contents 
except FileNotFoundError as e:
    print(e)
    print(path + " could not be found")
except PermissionError as e:
    print(e)
    print("You do not have permission to delete " + path)
except OSError as e:
    print(e)
    print("OS error")
else:
    print(path + " was deleted")
    print("The file is gone")