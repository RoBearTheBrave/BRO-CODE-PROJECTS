# sort() method = used with lists
# sorted() function = used with any iterable

students = ["Spongebob", "Patrick", "Squidward", "Sandy", "Mr. Krabs"]

# the sort() method sorts the list inplace (it changes the original list)
students.sort() # this method sorts the elements in ascending order (A-Z)
for i in students:
    print(i)


students.sort(reverse=True) # this method sorts the elements in descending order (Z-A)
for i in students:
    print(i)


# using the sorted() function
# the sorted() function returns a new list with the elements sorted in ascending order
students = ("Spongebob", "Plankton", "Gary", "Larry", "Mr. Krabs")
sorted_students = sorted(students) # this function returns a new list with the elements sorted in ascending order
for i in sorted_students:
    print(i)



# higher level sorting
# sorting a list of tuples
#create a list off tuples with name, grade, and age
students = [("Spongebob", 90, 30), 
            ("Patrick", 80, 31), 
            ("Squidward", 85, 32), 
            ("Sandy", 95, 33), 
            ("Mr. Krabs", 70, 34)]
print("-----------------sorting by grade-----------------")
grade = lambda grades: grades[1] # this lambda function will sort the list of tuples by the second element in each tuple
students.sort(key=grade) # this will sort the list of tuples by the first element in each tuple

for i in students:
    print(i)

print("-----------------sorting by age-----------------")
age = lambda ages: ages[2] # this lambda function will sort the list of tuples by the third element in each tuple
students.sort(key=age) # this will sort the list of tuples by the third element in each tuple

for i in students:
    print(i)