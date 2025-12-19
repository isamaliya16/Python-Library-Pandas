# 03_column_name_with_spaces.py

import pandas as pd

# Creating a DataFrame with column name containing spaces
data = {'first name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Using query with backticks for column name with spaces
result = df.query('`first name` == "Alice"')
print(result)
