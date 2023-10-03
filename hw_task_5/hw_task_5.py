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