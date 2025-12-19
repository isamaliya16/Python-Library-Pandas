# 20_query_with_different_data_types.py

import pandas as pd

# Creating a DataFrame with different data types
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32],
        'salary': [50000.50, 60000.75, 45000.25, 70000.00]}
df = pd.DataFrame(data)

# Using query with different data types
result = df.query('age > 25 & salary < 65000.00')
print(result)
