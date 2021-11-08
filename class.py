class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        return 2 * (self.a + self.b)

    def calc_surface(self):
        return self.a * self.b


class Square(Rectangle):
    def square_check(self):
        return self.a == self.b
