# copyfile() function copies files from one directory to another
# copy() = copyfile() + permisssion mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil   # the shutil module is a higher level file operations module that provides a higher level interface that is easier to use than the os module
                # the functions above are all in the shutil module

shutil.copyfile('test_file.txt', 'copy_test_file.txt') # this will copy the contents of test_file.txt to test_file_copy.txt

