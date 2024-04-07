# default arguments are used to provide a default value for a parameter
# if the caller does not provide a value for that parameter the default value is used
# this makes fucntions more flexible and reduces the number of arguments that need to be passed

#types of arguments: positional, keyword, default, variable-length(arbitrary)

# a function to calculate the net price of an item

def net_price(list_price, discount=0.00, tax=0.07):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(100))
#the default values used for discount and tax give us the ability to call the function with only the list_price
#we can also provide values for discount and tax if we want to


#create a count up timer

import time

#non default arguments must come before default arguments
#since the counter will typically start at 0, we can make that the default value for start
#the end value is required, so it is a non-default argument
#end must come before start in the parameter list because it is a non-default argument

def count(end, start=0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done")

count(5)
count(5, 2)