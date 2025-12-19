# 32_query_grouping_aggregation.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'],
        'department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
        'salary': [50000, 60000, 45000, 70000, 65000]}
df = pd.DataFrame(data)

# Using query with grouping and aggregation
df_grouped = df.groupby('department').salary.mean().reset_index()
result = df_grouped.query('salary > 50000')
print(result)
