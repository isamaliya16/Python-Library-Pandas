# creating_dataframe_with_index.py
import pandas as pd

# Creating a DataFrame with a custom index
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Display the DataFrame
print("DataFrame with a custom index:")
print(df)
