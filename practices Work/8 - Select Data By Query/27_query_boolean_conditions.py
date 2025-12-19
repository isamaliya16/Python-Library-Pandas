# 27_query_boolean_conditions.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'active': [True, False, True, False]}
df = pd.DataFrame(data)

# Using query with boolean conditions
result = df.query('active == True')
print(result)
