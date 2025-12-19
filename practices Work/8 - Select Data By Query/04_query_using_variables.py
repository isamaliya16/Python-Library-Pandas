# 04_query_using_variables.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using variables in query
min_age = 25
result = df.query('age > @min_age')
print(result)
