# resursion is a function that calls itself
# it is a way to solve problems by breaking them down into smaller problems
# it is a way to solve problems by defining a function in terms of itself
# it is a way to solve problems by reducing a problem to a simpler version of the same problem


# iterative approach
def walk(steps):
    for i in range(1, steps+1):
        print('step', i)




# recursive approach
# recursion is usually slower that iteration
# base case: the simplest possible version of the problem
# this works by removing steps from the call stack until the base case is reached

def walk_recursive(steps):
    if steps == 0:
        return
    walk_recursive(steps-1)
    print('step', steps)

#walk_recursive(100)



# iterative factorial
def factorial(n):
    result = 1
    if n == 0:
        for i in range(1, n+1):
            result *= i
        return result


# recursive factorial
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
print(factorial_recursive(5))