import numpy as np


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
