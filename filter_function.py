# the filter() creates a collection of elements from an iterable for which a function returns true.
# this is like a search result
# filter(function, iterable)
#name and age
friends = [("Alice", 25), 
           ("Bob", 30), 
           ("Charlie", 35), 
           ("Derek", 16)]


age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))
for i in drinking_buddies:
    print(i)