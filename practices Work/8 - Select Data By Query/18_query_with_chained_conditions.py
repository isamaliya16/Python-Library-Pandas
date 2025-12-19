# 18_query_with_chained_conditions.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32],
        'city': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Using query with chained conditions
result = df.query('(age > 25 & city == "NY") | (age < 30 & city == "SF")')
print(result)
