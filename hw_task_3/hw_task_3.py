import random

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


class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.ag = age
        self.gender = gender


class Student(Human):    # задание 2 + задание 3

    def __init__(self, name, age, gender, knowledge=[]):
        self.knowledge = knowledge
        super().__init__(name, age, gender)

    def take(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def info(self):
        print(self.knowledge)

    def forget(self):
        random_element = random.choice(self.knowledge)
        self.knowledge.remove(random_element)

    def __len__(self):
        return len(self.knowledge)

class Teacher(Human):

    def __init__(self, name, age, gender, num_teached=0, course=0):
        self.num_teached = num_teached
        self.course = course
        super().__init__(name, age, gender)

    def teach(self, material, *args):
        for i in args:
            i.take(material.study[self.course])
            self.num_teached += 1
        self.course += 1

    def info(self):
        print(self.num_teached)


class Material:

    def __init__(self, *args):
        self.study = []
        for i in args:
            self.study.append(i)

    def course(self):
        print(self.study)

    def __len__(self):
        return len(self.study)


my_materials = Material('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')

student_1 = Student('Sergey', 33, 'male', ['1'])
student_2 = Student('Dmitriy', 18, 'male', ['2'])
student_3 = Student('Oxana', 25, 'female', ['3'])
student_4 = Student('Olga', 46, 'female', ['4'])

teacher = Teacher('Semen', 27, 'male')

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

student_4.forget()
student_4.info()

print(len(my_materials))
print(len(student_1))


class Apple:

    def __init__(self, index, phase='bloom'):
        self.index = index
        self.phase = phase
        self.phases = ['bloom', 'green', 'red']

    def grow(self):
        if self.phase == 'bloom':
            self.phase = 'green'
        elif self.phase == 'green':
            self.phase = 'red'

    def good(self):
        return self.phase == 'red'


class Tree:

    def __init__(self, *args):
        self.apple_list = []
        self.args = args
        for i in args:
            self.apple_list.append(i.index)
        print(self.apple_list)

    def harvest(self):
        self.apple_list = []

    def grow_tree(self):
        for i in self.args:
            i.grow()

    def good_tree(self):
        for i in self.args:
            if i.good() == False:
                return False
        return True


class Gardener:

    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def fertilize(self):
        for i in self.args:
            i.grow_tree()


    def collect(self):
        for i in self.args:
            if i.good_tree() == True:
                i.harvest()
                print('Collected')
            else:
                print('Not yet')


apple_1 = Apple(1)
apple_2 = Apple(2)
apple_3 = Apple(3)
apple_4 = Apple(4)
apple_5 = Apple(5)
# print(apple_4.good())
# apple_4.grow()
# print(apple_4.good())
# apple_4.grow()
# print(apple_4.good())

tree = Tree(apple_1, apple_2, apple_3, apple_4, apple_5)
gardener = Gardener('Denis', tree)
gardener.collect()
gardener.fertilize()
gardener.collect()
gardener.fertilize()
gardener.collect()
