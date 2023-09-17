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


class Student():    # задание 2

    def __init__(self, knowledge=[]):
        self.knowledge = knowledge

    def take(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def info(self):
        print(self.knowledge)

class Teacher():

    def __init__(self, num_teached=0, course=0):
        self.num_teached = num_teached
        self.course = course

    def teach(self, material, *args):
        for i in args:
            i.take(material.study[self.course])
            self.num_teached += 1
        self.course += 1

    def info(self):
        print(self.num_teached)


class Material():

    def __init__(self, *args):
        self.study = []
        for i in args:
            self.study.append(i)

    def course(self):
        print(self.study)


my_materials = Material('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')

student_1 = Student(['1'])
student_2 = Student(['2'])
student_3 = Student(['3'])
student_4 = Student(['4'])
teacher = Teacher()

teacher.teach(my_materials, student_1, student_2)
teacher.teach(my_materials, student_2, student_3)
teacher.teach(my_materials, student_1, student_2, student_3, student_4)
teacher.teach(my_materials, student_4)
teacher.teach(my_materials, student_4)
student_1.info()
student_2.info()
student_3.info()
student_4.info()
teacher.info()