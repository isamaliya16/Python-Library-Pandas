# 33_query_with_category_dtype.py

import pandas as pd

# Creating a DataFrame with category data type
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'department': ['HR', 'IT', 'Finance', 'HR']}
df = pd.DataFrame(data)
df['department'] = df['department'].astype('category')

# Using query with category data type
result = df.query('department == "HR"')
print(result)
