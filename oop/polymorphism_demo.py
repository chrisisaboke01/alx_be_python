import math

class Shape:
    def area(self):
        """
        This method should be overridden by subclasses to calculate the area.
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Rectangle class that inherits from Shape.
        Initializes the rectangle's length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Override the area method to calculate the area of the rectangle.
        Area formula: length × width
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Circle class that inherits from Shape.
        Initializes the circle's radius.
        """
        self.radius = radius

    def area(self):
        """
        Override the area method to calculate the area of the circle.
        Area formula: π × radius²
        """
        return math.pi * (self.radius ** 2)
