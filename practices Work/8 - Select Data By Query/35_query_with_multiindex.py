# 35_query_with_multiindex.py

import pandas as pd

# Creating a DataFrame with MultiIndex
arrays = [['Alice', 'Alice', 'Bob', 'Bob'], ['Math', 'Science', 'Math', 'Science']]
index = pd.MultiIndex.from_arrays(arrays, names=('name', 'subject'))
data = {'score': [85, 95, 78, 88]}
df = pd.DataFrame(data, index=index)

# Using query with MultiIndex
result = df.query('name == "Alice"')
print(result)
