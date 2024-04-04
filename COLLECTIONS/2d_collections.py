# 2D collections are used to store data in a table format.
# 2D collections are baically lists within lists.
# you can also store tuples, or sets within 2D collections.
# 2D collections are used to store data in a table format.




#each of these lists are one dimensional lists
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato", "spinach"]
meat = ["chicken", "beef", "pork"]


#2D list
#if you index over grocery_list, you will get a one dimensional list for each of the items in the grocery_list
grocery_list = [fruits, vegetables, meat]

#to access individual items in the 2D list, you need to index twice like so: grocery_list[0][0] will give you "apple"
print(grocery_list)


#2D lists don't need to have inner lists stored inside variables
#this can be set up like this instead
grocery_list = [["apple", "banana", "cherry"], ["carrot", "potato", "spinach"], ["chicken", "beef", "pork"]]

#to make this more readable, you can do this
grocery_list = [
    ["apple", "banana", "cherry"],
    ["carrot", "potato", "spinach"],
    ["chicken", "beef", "pork"]
]

#you can iterate over a 2D list like so
for items in grocery_list:
    for food in items:
        print(food)