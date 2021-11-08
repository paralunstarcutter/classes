class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def p(self):
        return 2*(self.a + self.b)
    def s(self):
        return self.a * self.b
class Square(Rectangle):
    def sq(self):
        if self.a == self.b:
            self.sq = True
            return self.sq
        else:
            self.sq = False
            return self.sq



#x = Square(2,10)
#y = Square(10,10)
#print(x.p())
#print(x.s())
#print(x.sq())
#print(y.p())
#print(y.s())
#print(y.sq())

# Добрий день, це Репіна Софія. Надалі буду (намагатися) відсилати роботи через GitHub