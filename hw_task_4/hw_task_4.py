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