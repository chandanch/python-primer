# Class - A class is a blue print for creating new objects
# Object - An object is an instance of a class
"""
    Class point
"""


class Point:
    """
        Point class
    """
    # __init__() is a special method which represents the constructor,
    # the constructor is called when creating an instance of the class
    # *self* parameter is a pointer or reference to the current instance of the class.
    # Basically it points to the current instance of the class which can be used to access
    # instance members such as attributes & methods of a class

    # The below is a class attribute which is shared by all instances of a class
    default_color = 'Red'

    def __init__(self, xcoord, ycoord):

        self.xcoord = xcoord
        self.ycoord = ycoord

    # classs method - Bound to the class itself. they return the instance of the class
    # Class method is method that is called on the class itself, not on a specific object instance. Therefore, it belongs to a class level, and all class instances share a class method.
    # Class methods are like factory methods that initializes the instance of the class with some default values
    @classmethod
    def initialize_values(cls):
        return cls(0, 0)

    def draw(self):
        """
            Drawing
        """
        print(f"Drawing on {self.xcoord} {self.ycoord}")


# Create an instance of point
new_point = Point(23, 55)
# Instance attribute - These attributes are scoped to a specific instance of a class
# new_point.default_color = 'green'
new_point.draw()
print(new_point.default_color)


line_point = Point(78, 98)
line_point.default_color = 'blue'

print(line_point.default_color)

# Accessing class attributes through Class reference
Point.default_color = 'Velvet'
print(line_point.default_color, new_point.default_color)

jp_point = Point.initialize_values()

jp_point.__str__()