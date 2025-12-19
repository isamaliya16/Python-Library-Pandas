# 14_query_with_regular_expressions.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['New York', 'Los Angeles', 'San Francisco', 'New York']}
df = pd.DataFrame(data)

# Using query with regular expressions
result = df.query('city.str.contains("New|Los")', engine='python')
print(result)
