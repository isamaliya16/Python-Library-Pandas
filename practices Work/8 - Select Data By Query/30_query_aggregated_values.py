# 30_query_aggregated_values.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'score': [85, 90, 75, 95]}
df = pd.DataFrame(data)

# Using query with aggregated values
avg_score = df['score'].mean()
result = df.query('score > @avg_score')
print(result)
