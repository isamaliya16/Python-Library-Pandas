# 10_query_with_date_column.py

import pandas as pd

# Creating a DataFrame with a date column
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'birthdate': ['1990-01-01', '1985-05-05', '1992-09-09', '1980-12-12']}
df = pd.DataFrame(data)
df['birthdate'] = pd.to_datetime(df['birthdate'])

# Using query with date column
result = df.query('birthdate > "1990-01-01"')
print(result)
