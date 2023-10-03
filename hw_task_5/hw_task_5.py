import pandas as pd
import numpy as np


m = np.random.randint(1, high=11, size=100, dtype=int).reshape((10,10)) # задание 1
df = pd.DataFrame(m)


ind = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']    # задание 2
df.index = ind
df = df[(df > 5).all(axis=1)]
if not df.empty:
    print(df)
else:
    print('No line with all values > 5')


m = np.random.randint(1000, size=100, dtype=int).reshape((10,10)) # задание 3
df = pd.DataFrame(m)
ind = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = ind
df.columns = ind
print('Matrix shape is', df.shape)
print('Matrix rows are', list(df.index))
print('Matrix columns are', list(df.columns))
print('Matrix mean is', df.mean().mean())
df.to_csv('Matrix_task_3.csv')


df = pd.read_csv('emojis.csv')  # задание 4
sub = df.groupby('Subcategory')['Rank'].sum()
print(sub[sub == sub.min()])


