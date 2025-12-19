# 18_dataframe_values.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Viewing DataFrame values
print(df.values)
