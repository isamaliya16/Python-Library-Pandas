# 38_query_with_index_resetting.py

import pandas as pd

# Creating a DataFrame with index
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

# Using query and resetting index
result = df.query('age > 25').reset_index(drop=True)
print(result)
