# 23_query_complex_expressions.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with complex expressions
result = df.query('age % 2 == 0')
print(result)
