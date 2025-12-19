# 28_query_numeric_ranges.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query to filter numeric ranges
result = df.query('age.between(25, 30)')
print(result)
