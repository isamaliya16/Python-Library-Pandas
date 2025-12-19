# 29_query_isin.py

import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['New York', 'Los Angeles', 'San Francisco', 'New York']}
df = pd.DataFrame(data)

# Using query with `isin` method
result = df.query('city.isin(["New York", "San Francisco"])')
print(result)
