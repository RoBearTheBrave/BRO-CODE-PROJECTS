# a dictionary is a collection of key-value pairs
# each key is connected to a value {key: value}
# a key's value can be a number, a string, a list, or even another dictionary
# dictionaries are mutable
# dictionaries are unordered
# dictionaries are indexed by keys
# no duplicate keys are allowed

# example of a dictionary
# {id: name}

# create a dictionary
capitals = {"USA": "Washington D.C.", 
            "France": "Paris", 
            "Germany": "Berlin",
            "Italy": "Rome"
            }

# you can use dir() to see what methods are available for dictionaries
# print(dir(capitals))


print(capitals.get("USA")) #this will return the value for the key "USA"


print(capitals.get("Canada")) #this will return None because "Canada" is not a key in the dictionary

#use .get to check for a key in a dictionary
#create a conditional statement to check for a key against our dictionary
if capitals.get("") == None:
    print("That is not in the dictionary")

capitals.update({"Canada": "Ottawa"}) #this will add or update a key: value. now "Canada": "Ottawa" to the dictionary

print(capitals.get("Canada")) #this will return "Ottawa"


#use pop() to remove a key from a dictionary
capitals.pop("Canada") #this will remove "Canada" from the dictionary
print(capitals.get("Canada")) #this will return None because "Canada" is not a key in the dictionary


#use popitem() to remove the last key-value pair from a dictionary
capitals.popitem() #this will remove the last key-value pair from the dictionary
print(capitals)



#to get all of the key, but not the values, use .keys()
print(capitals.keys()) #this will return a list of all the keys in the dictionary


for key in capitals.keys():
    print(key)


# use the values() method to get all of the values in a dictionary
print(capitals.values()) #this will return a list of all the values in the dictionary

for value in capitals.values():
    print(value)



#use the items() method to get all of the key-value pairs in a dictionary
print(capitals.items()) #this will return a list of tuples for each key-value pair in the dictionary
#this will return a list of tuples for each key-value pair in the dictionary

for key, value in capitals.items():
    print(f"{key}: {value}")
