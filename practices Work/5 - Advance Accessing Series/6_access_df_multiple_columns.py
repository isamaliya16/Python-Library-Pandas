# access_df_multiple_columns.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Accessing multiple columns
print(df[['Name', 'City']])
