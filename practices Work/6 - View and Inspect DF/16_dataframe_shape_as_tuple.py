# 16_dataframe_shape_as_tuple.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Viewing the shape of the DataFrame as tuple
print(df.shape)
