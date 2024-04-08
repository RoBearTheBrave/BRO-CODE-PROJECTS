# list comprehension is a concise way to create lists with less syntax
# it is a more readable way to create lists
# it is more efficient than using a for loop

# syntax: list = [expression for item in iterable]


squares = []                # create an empty list
for i in range(1, 11):      # create a for loop that iterates through the numbers 1-10
    squares.append(i * i)   # define what each loop iteration should do
print(squares)


# using list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)


#filter a list of student grades to only include passing grades

student_grades = [90, 85, 50, 60, 70, 30, 20, 100, 95]

passing_grades = list(filter(lambda grade: grade >= 70, student_grades))
print(passing_grades)

#using list comprehension
passing_grades = [grade for grade in student_grades if grade >= 70]
print(passing_grades)

# list comprehension with if else
# create a list of passing grades and failing grades
# passing grades are 70 or higher
# failing grades are below 70
passing_grades = [grade if grade >= 70 else "Failed" for grade in student_grades]
print(passing_grades)