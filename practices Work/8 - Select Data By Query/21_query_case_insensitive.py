# 21_query_case_insensitive.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['New York', 'los Angeles', 'San Francisco', 'NEW YORK']}
df = pd.DataFrame(data)

# Using query with case-insensitive string matching
result = df.query('city.str.lower() == "new york"', engine='python')
print(result)
