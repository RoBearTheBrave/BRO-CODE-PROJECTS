# The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class.


class Rectangle:
   def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
   
    def __init__(self, length, width):
        super().__init__(length, length)
    
    def cube(self, length, width, height):
        super().__init__(length, width)
        self.height = height