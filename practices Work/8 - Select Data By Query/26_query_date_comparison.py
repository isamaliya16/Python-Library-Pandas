# 26_query_date_comparison.py

import pandas as pd

# Creating a DataFrame with dates
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'start_date': ['2023-01-01', '2022-05-15', '2021-09-10', '2023-06-20']}
df = pd.DataFrame(data)
df['start_date'] = pd.to_datetime(df['start_date'])

# Using query with date comparison
result = df.query('start_date > "2022-12-31"')
print(result)
