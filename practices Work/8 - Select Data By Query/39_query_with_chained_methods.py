# 40_query_with_chained_methods.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32],
        'salary': [50000, 60000, 45000, 70000]}
df = pd.DataFrame(data)

# Using query with chained method calls
result = df.query('age > 25').sort_values(by='salary', ascending=False)
print(result)
