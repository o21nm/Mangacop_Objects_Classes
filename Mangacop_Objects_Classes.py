import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * (self.radius ** 2)
        print(f"The area of the circle with radius {self.radius} is: {circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle with radius {self.radius} is: {circle_perimeter:.2f}")

radius_value = 5
my_circle = Circle(radius_value)

my_circle.area()
my_circle.perimeter()
