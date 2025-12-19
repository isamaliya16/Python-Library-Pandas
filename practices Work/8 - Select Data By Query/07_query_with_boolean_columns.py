# 07_query_with_boolean_columns.py

import pandas as pd

# Creating a DataFrame with a boolean column
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'is_student': [True, False, True, False]}
df = pd.DataFrame(data)

# Using query with boolean column
result = df.query('is_student == True')
print(result)
