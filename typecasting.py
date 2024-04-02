#typecasting == the process of converting a value of one data type to another 
# works on (string, integer, float, boolean)
# can be done explicitly or implicitly 


#Explict typecasting
name = "Bro"
age = 39
gpa = 3.5
student = True


#find the type 
type(age)
print(type(age))

#change the type explicitly 
age = float(age)
print(age)


#implicitly convertly a value or variable automatically
x = 2
y = 2.0

x = x/y
print(type(x))