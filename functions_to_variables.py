# assigninig functions to variables


    
def hello():
    print("Hello")

print(hello) #this will print the memory location of the function hello
hi = hello #this will assign the function hello to the variable hi
print(hi) #this will print the memory location of the function hello
hi() #this will call the hello function

say = print
say("Whoa! This is a cool way to call the print function using a variable!")
#if I need to print something to the console, I can use the variable say instead of print