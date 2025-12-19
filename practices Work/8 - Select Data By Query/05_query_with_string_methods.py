# 05_query_with_string_methods.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['New York', 'Los Angeles', 'San Francisco', 'New York']}
df = pd.DataFrame(data)

# Using query with string methods
result = df.query('city.str.contains("New")', engine='python')
print(result)
