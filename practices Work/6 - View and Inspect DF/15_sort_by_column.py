# 15_sort_by_column.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Sorting by column 'Age'
print(df.sort_values(by='Age'))

