# 22_query_string_length.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David']}
df = pd.DataFrame(data)

# Using query to filter based on string length
result = df.query('name.str.len() > 3', engine='python')
print(result)
