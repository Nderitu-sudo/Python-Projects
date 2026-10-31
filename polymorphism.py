
#Polymorphism means “many forms”: the same interface (method name, operator, or function) behaves differently depending on the object it’s used with.
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
        return 3.14 * self.radius * self.radius

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 2)]

for shape in shapes:
    print(shape.area())