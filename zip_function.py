# the zip function is used to combine two or more iterables into a single iterable
# the zip function returns a zip object with paired elements stored in an iterator of tuples
# the zip function will aggregate elements from two or more iterables


usernames = ["Alice", "Bob", "Charlie"]
passwords = ["123", "456", "789"]

users = zip(usernames, passwords)
for i in users:
    print(i)


# the zip function is of type zip, but you can cast it to another type
# you can cast it to a list
users = list(zip(usernames, passwords))
print(users)

# you can cast it to a set
users = set(zip(usernames, passwords))
print(users)

# you can cast it to a dictionary
users = dict(zip(usernames, passwords))
print(users)

for key, value in users.items(): #items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
    print(key+ " : " +value)


# using zip object with more than two iterables
usernames = ["Alice", "Bob", "Charlie"]
passwords = ["123", "456", "789"]
security_questions = ["What is your favorite color?", "What is your favorite food?", "What is your favorite movie?"]

users2 = zip(usernames, passwords, security_questions)
for i in users2:
    print(i)