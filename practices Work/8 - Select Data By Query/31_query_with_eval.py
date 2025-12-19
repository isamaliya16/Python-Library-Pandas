# 31_query_with_eval.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32],
        'salary': [50000, 60000, 45000, 70000]}
df = pd.DataFrame(data)

# Using query with `eval` function
result = df.query('age + salary / 1000 > 50')
print(result)
