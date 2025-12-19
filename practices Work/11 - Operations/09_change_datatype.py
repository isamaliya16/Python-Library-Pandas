# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4.0, 5.5, 6.1]}
df = pd.DataFrame(data)

# Changing data type of a column
df['B'] = df['B'].astype(int)

# Printing the DataFrame with changed data type
print("DataFrame with changed data type of column B:")
print(df)
