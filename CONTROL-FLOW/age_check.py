# if = Do some code only IF some condition is True
#       Else do something else

age = int(input("Enter you age: "))

if age >= 100: #ensure the condition checks are in the right order
    print("You are too old")
elif age < 0:
    print("You are not alive yet!")
elif age >= 18:
    print("You are now signed up!")
else: #if no above conditions are true (like a default)
    print("You must be 18+ to sign up")