# 06_query_with_math_operations.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'salary': [50000, 60000, 45000, 70000]}
df = pd.DataFrame(data)

# Using query with mathematical operations
result = df.query('salary > 50000 * 1.1')
print(result)
