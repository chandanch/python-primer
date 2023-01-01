# Class - A class is a blue print for creating new objects
# Object - An object is an instance of a class

class Point:
    """
        Point class
    """
    def draw(self):
        """
            Drawing
        """
        print("Drawing point")

# Create an instance of point
new_point = Point()
print(new_point.draw())