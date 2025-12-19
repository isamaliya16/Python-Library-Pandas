# 17_dataframe_size.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Girish'],
        'Age': [28, 24, 35, 32, 34]}
df = pd.DataFrame(data)

# Viewing the size of the DataFrame
print(df.size)
