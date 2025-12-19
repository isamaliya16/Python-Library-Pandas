# 02_multiple_conditions.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32],
        'city': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Using query to select rows where age > 25 and city is 'NY'
result = df.query('age > 25 & city == "NY"')
print(result)
