# using map() function = applies a given function to all the items in an input_list

# map(function, input_list)

# the map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc.)


#convert prices to bht
store_prices = [("shirt", 20), 
                ("pants", 30), 
                ("shoes", 50)]

to_bht = lambda data: (data[0], data[1] * 33.24)
to_dollar = lambda data: (data[0], data[1] / 33.24)

store_dollars = list(map(to_bht, store_prices))

for i in store_dollars:
    print(i)


