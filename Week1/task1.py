import math

# Процедурний підхід
def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2

# Обчислення площ у процедурному підході
rect_area_proc = rectangle_area(5, 3)
circle_area_proc = circle_area(4)

print("Процедурний підхід:")
print("Площа прямокутника:", rect_area_proc)
print("Площа кола:", circle_area_proc)



# Об'єктно орієнтований підхід


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Обчислення площ в об’єктноорієнтованому підході
rectangle = Rectangle(5, 3)
circle = Circle(4)

print("")
print("Об’єктноорієнтований підхід:")
print("Площа прямокутника:", rectangle.area())
print("Площа кола:", circle.area())
