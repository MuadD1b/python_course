import numpy as np
import re
import pandas as pd


m = np.random.randint(1, high=11, size=10, dtype=int) # задание 1
print('task 1')
print(sorted(m))
print()


x = np.zeros((8,8),dtype=int)   # задание 2
print('task 2')
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)
print()


m = np.random.randint(1, high=11, size=32, dtype=int).reshape(8, 4) # задание 3
n = np.random.randint(1, high=11, size=8, dtype=int).reshape(4, 2)
print('task 3')
print(np.dot(m, n))
print()


m = np.random.rand(10) # задание 4
for i in range(len(m)):
    while m[i] == 0:
        m[i] = np.random.random()
print('task 4')
print(m)
print()


def matrix(N:int):  # задание 5
    m = int(N/2)
    count = 0
    for i in range(2, m + 1):
        if N % i == 0:
            count += 1
            n = int(N/i)
            print(f'Matrix {count}: ({i} * {n}) ')
            print(np.random.randint(1, high=11, size=N, dtype=int).reshape(i, n))
    if count == 0:
        print('No matrixes could be created')


print('task 5')
matrix(12)
print()


class text_search:    # задание 6

    def __init__(self, path):
        self.path = path

    def read(self):
        self.text = np.genfromtxt(self.path, dtype=str, delimiter='\n')
        self.line = ''
        for i in self.text:
            self.line += i

    def search(self, pattern):
        self.match = re.findall(fr'{pattern}', self.line)
        print(self.match)


print('task 6')
text = text_search('text.txt')
text.read()
text.search('\d\w{3}\d')
print()


def forward(A, S, last=False):    # задание 7
    X = len(A)
    B = np.random.rand(S * X).reshape(S, X)
    M = np.dot(B, A)
    if last == False:
        res = np.sin(M)
    else:
        res = np.maximum(M, 0)
    return res, B


print('task 7')
vec = np.random.rand(5)
x1, B1 = forward(vec, 10)
x2, B2 = forward(x1, 10)
x3, B3 = forward(x2, 5, True)
print(x3 * 100)
print()


class analise:    # задание 8

    def __init__(self, path):
        self.path = path

    def read(self):
        self.text = pd.read_csv(self.path)
        print(self.text)


print('task 8')
nlo = analise('nlo.csv')
nlo.read()
print()