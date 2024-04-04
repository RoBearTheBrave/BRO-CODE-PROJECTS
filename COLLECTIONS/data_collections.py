# collection is basically a single "variable" that holds multiple items
# collections are also called data structures
# there are four types of collections in Python:
#     1. list - [] a collection of items that are ordered and changeable. Allows duplicate members.
#     2. tuple - () a collection of items that are ordered and unchangeable. Allows duplicate members.
#     3. set - {} a collection of items that are unordered and unindexed. No duplicate members.
#     4. dictionary - {} a collection of items that are unordered, changeable and indexed. No duplicate members.


#####-----------------LISTS-----------------#####
# # ordered and changeable. Allows duplicate members.
# # [] - square brackets

#it can be helpful to make the name of a list plural to indicate that it is a collection of items
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

print(fruits[1:4:2])
# output: ['banana', 'date']

for fruit in fruits:
    print(fruit)

#use the dir() function to see all the methods available for a list
#print(dir(fruits))
    #output: is a list of __attributes__ and methods for a list
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    
#use the help() function to get more information on a method
    
len(fruits) #returns the number of items in the list   
print(fruits[1]) #prints the second item in the list

#use the in operator to check if an item is in the list
print("banana" in fruits) #prints True

#lists are mutable, meaning you can change the items in a list
fruits[1] = "blackberry"
print(fruits) #prints the list with "blackberry" in place of "banana"

#use the append method to add an item to the end of a list
fruits.append("kiwi")
print(fruits) #prints the list with "kiwi" added to the end

#use remove to remove an item from a list
fruits.remove("date")
print(fruits) #prints the list with "date" removed

#use the insert method to add an item to a specific index in the list
fruits.insert(2, "blueberry")
print(fruits) #prints the list with "blueberry" added at index 2

#sort the list in alphabetical order
fruits.sort()
print(fruits) #prints the list in alphabetical order

#use the reverse method to reverse the order of the list
fruits.reverse()
print(fruits) #prints the list in reverse order from how they were entered into the list    

#for reverse alphabetical order, use the sort method with the reverse parameter set to True
fruits.sort(reverse=True)
print(fruits) #prints the list in reverse alphabetical order

#to clear all items from a list, use the clear method
fruits.clear()
print(fruits) #prints an empty list


#####-----------------SETS-----------------#####
# # unordered and unindexed. No duplicate members.
# sets are mutable, meaning you can change the items in a set
# # {} - curly brackets

#sets are useful for removing duplicates from a list

fruits = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "banana"}

print(dir(fruits))
    #output: is a list of __attributes__ and methods for a set
    # there are some more advanced methods for sets than for lists

fruits.add("kiwi")
fruits.remove("date")
fruits.pop() #removes the last item in the set


#####-----------------TUPLES-----------------####
# # ordered and unchangeable. Allows duplicate members.
# # () - parentheses
# tuples are immutable, meaning you cannot change the items in a tuple
# tuples are useful when you want to store a collection of items that should not be changed
# tuples are faster than lists

fruits = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape")


# #use the dir() function to see all the methods available for a tuple
# the methods available for a tuple are similar to those for a list



#####-----------------DICTIONARIES-----------------#####
#covered in dictionaries.py