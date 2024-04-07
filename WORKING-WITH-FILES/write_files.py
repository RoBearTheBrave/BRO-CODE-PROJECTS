
path = "/Users/robertthibault/Projects/BRO-CODE/BRO-CODE-PROJECTS/test_write_file.txt"


text = 'This is a test string\nThis is the second line\nThis is the third line'
text = "This is going to write over the first text"


with open(path, 'w') as file: 
        print(file.write(text))

text = "\nThis is going to be appended to the file"

with open(path, 'a') as file: 
        print(file.write(text))