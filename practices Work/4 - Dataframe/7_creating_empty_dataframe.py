# creating_empty_dataframe.py
import pandas as pd

# Creating an empty DataFrame
df = pd.DataFrame()

# Adding columns to the DataFrame
df['Name'] = ['Alice', 'Bob', 'Charlie']
df['Age'] = [25, 30, 35]
df['City'] = ['New York', 'Los Angeles', 'Chicago']

# Display the DataFrame
print("Empty DataFrame with added columns:")
print(df)

