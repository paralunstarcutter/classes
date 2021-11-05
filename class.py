class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        # Бажано, щоб назва функції відповідала на питання, що робить ця функція.
        return 2 * (self.a + self.b)

    def calc_surface(self):
        return self.a * self.b


class Square(Rectangle):
    def square_check(self):
        # Невеличкий lifehack, якщо в тебе функція перевіряє True або False, можеш просто зробити так
        return self.a == self.b

# Перед выдправкою коду на перевірку, краще видаляй закоментовані частинки коду нижче. Буде виглядати "професійніше" ) 

#x = Square(2,10)
#y = Square(10,10)
#print(x.p())
#print(x.s())
#print(x.sq())
#print(y.p())
#print(y.s())
#print(y.sq())

# Добрий день, це Репіна Софія. Надалі буду (намагатися) відсилати роботи через GitHub
