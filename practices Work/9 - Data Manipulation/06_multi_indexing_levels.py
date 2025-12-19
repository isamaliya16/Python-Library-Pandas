import pandas as pd

# Creating a MultiIndex DataFrame
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2)])
data = {'Value': [100, 200, 300, 400]}
df = pd.DataFrame(data, index=index)
df.index.names = ['Letter', 'Number']

# Accessing different levels of MultiIndex
print(df.index.levels[0])
print(df.index.levels[1])
