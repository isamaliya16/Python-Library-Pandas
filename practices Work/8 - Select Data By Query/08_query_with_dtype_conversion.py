# 08_query_with_dtype_conversion.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': ['24', '27', '22', '32']}  # age as strings
df = pd.DataFrame(data)

df['age'] = df['age'].astype(int)
result = df.query('age > 25')
print(result)
