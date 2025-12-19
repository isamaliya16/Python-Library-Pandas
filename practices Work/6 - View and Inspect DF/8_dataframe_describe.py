# 08_dataframe_describe.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Salary': [50000, 60000, 75000, 85000]}
df = pd.DataFrame(data)

# Viewing summary statistics
print(df.describe())
