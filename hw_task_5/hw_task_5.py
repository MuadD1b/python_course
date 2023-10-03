import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


m = np.random.randint(1, high=11, size=100, dtype=int).reshape((10,10)) # задание 1
df = pd.DataFrame(m)
print('task 1')
print()

ind = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']    # задание 2
print('task 2')
df.index = ind
df = df[(df > 5).all(axis=1)]
if not df.empty:
    print(df)
else:
    print('No line with all values > 5')
print()


m = np.random.randint(1000, size=100, dtype=int).reshape((10,10)) # задание 3
print('task 3')
df = pd.DataFrame(m)
ind = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = ind
df.columns = ind
print('Matrix shape is', df.shape)
print('Matrix rows are', list(df.index))
print('Matrix columns are', list(df.columns))
print('Matrix mean is', df.mean().mean())
df.to_csv('Matrix_task_3.csv')
print()


df = pd.read_csv('emojis.csv')  # задание 4
print('task 4')
sub = df.groupby('Subcategory')['Rank'].sum()
print(sub[sub == sub.min()])
print()


df = pd.read_csv('emojis.csv')  # задание 5
print('task 5')
plt.plot(df.groupby(['Year']).size())
plt.savefig('New_vs_Year.png')
print()


def check_category(cat: str):   # задание 6
    df = pd.read_csv('emojis.csv')
    df = df.groupby(['Category']).size()
    total = df.sum()
    if cat in df:
        print(f'Category "{cat}" is {df.loc[cat] / total * 100} %')
    else:
        print(f'Category "{cat}" is not in emojis')


print('task 6')
check_category('Flags')
check_category('Life')
print()