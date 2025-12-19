# 13_query_with_compound_expressions.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with compound expressions
result = df.query('age > 25 | name == "Alice"')
print(result)
