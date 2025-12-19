import pandas as pd

# Creating a MultiIndex DataFrame
arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Number'))

data = {'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data, index=index)

# Resetting the index
df_reset = df.reset_index()
print(df_reset)
