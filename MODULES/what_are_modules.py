# a module is a file containing code you want to include in your application
# a module can contain functions, classes, and variables
# you can import a module into your application using the import statement
# they are useful to breakup large programs into smaller, reusable pieces, in separate files -- this makes the code easier to read, maintain, and organize

# to find standard modules, you can search the Python Standard Library
#print(help("modules"))

# to find third-party modules, you can search the Python Package Index (PyPI)
# you can install third-party modules using pip, the package installer for Python

################### you can create your own modules by creating a file with a .py extension ####################
# when you create your own modules you can import them into your application using the import statement just like you would with a standard module and use the functions, classes, and variables in your application

import math

print(math.pi)

# you can give modules an alias when you import them by using the as keyword
import math as m

print(m.pi)

# you can import specific functions, classes, or variables from a module using the from keyword

from math import pi # this can lead to naming conflicts, so be careful



