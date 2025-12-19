# 36_query_with_inplace.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with `inplace` parameter
df.query('age > 25', inplace=True)
print(df)
