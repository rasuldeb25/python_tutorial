#super() = function in child class to call methods from a present class (superclasses)
#           allows you to extend the functionality of the inherited class

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"This shape is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, radius, color, is_filled):
        self.radius = radius
        super().__init__(color, is_filled)

    def describe(self):
        print(f"It is a circle with a area of {3.14 * self.radius ** 2}")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with a area of {self.width ** 2}")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a triangle with a area of {0.5 * self.width * self.height}")
        super().describe()


circle = Circle(10, "red", True)

print(circle.radius)
print(circle.color)
print(circle.is_filled)
circle.describe()

square = Square("blue", False, 5)

print(square.color)
print(square.is_filled)
print(square.width)
square.describe()

triangle = Triangle("green", True, 8, 6)

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()