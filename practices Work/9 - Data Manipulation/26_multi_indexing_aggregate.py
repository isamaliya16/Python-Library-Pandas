import pandas as pd

# Creating a MultiIndex DataFrame
arrays = [['X', 'X', 'Y', 'Y'], ['Red', 'Blue', 'Red', 'Blue']]
index = pd.MultiIndex.from_arrays(arrays, names=('Letter', 'Color'))

data = {'Count': [5, 15, 25, 35]}
df = pd.DataFrame(data, index=index)

# Aggregating data using MultiIndex
print(df.groupby(level='Letter').sum())
