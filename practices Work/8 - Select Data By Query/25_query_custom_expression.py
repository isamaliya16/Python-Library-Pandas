# 25_query_custom_expression.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'score': [85, 90, 75, 95]}
df = pd.DataFrame(data)

# Using query with custom expression
result = df.query('score >= 85')
print(result)
