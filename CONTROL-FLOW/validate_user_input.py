#validate user input
##Rules:
# username is no more than 12 characters
# username must not contain spaces
# username nust not cantain digits

prompt = "Enter your username: "
username = input(prompt)


while True: #this loop will continue to run until the user enters a valid username
    if len(username) > 12:
        print("Username must be 12 characters or less")
        username = input(prompt)
    elif username.find(" ") != -1: #if the username contains a space, the find method will return the index of the space
        print("Username must not contain spaces")
        username = input(prompt)
    elif not username.isalpha():
        print("Username must not contain digits")
        username = input(prompt)
    else:
        print(f"Welcome, {username}")
        break #this will break the loop if the username is valid
