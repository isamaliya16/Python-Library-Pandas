# 17_query_with_aliases.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with aliases
result = df.query('age > 25 and age < 30').rename(columns={'age': 'years'})
print(result)
