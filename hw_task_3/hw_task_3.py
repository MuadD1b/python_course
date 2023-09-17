class Rectangle:    # задание 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print('Area = ', self.a * self.b)

    def perimetr(self):
        print('Perimetr = ', 2 * self.a * self.b)


my_rec = Rectangle(2, 10)
my_rec.area()
my_rec.perimetr()