# using the reduce function applies a function of our choosing to the FIRST TWO ELEMENTS of an iterable AND THEN REPEATS THE PROCESS UNTIL THERE IS ONLY ONE ELEMENT LEFT
# the reduce function is part of the functools module

#reduce(function, iterable)
import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters) #this will concatenate each value in the list until there is only one value left
print(word)


#using the reduce function to find the maximum value in a list
factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result) #this will multiply each value in the list until there is only one value left