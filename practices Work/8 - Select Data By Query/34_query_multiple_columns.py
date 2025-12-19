# 34_query_multiple_columns.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32],
        'city': ['New York', 'Los Angeles', 'San Francisco', 'New York']}
df = pd.DataFrame(data)

# Using query with multiple columns
result = df.query('age > 25 & city == "New York"')
print(result)
