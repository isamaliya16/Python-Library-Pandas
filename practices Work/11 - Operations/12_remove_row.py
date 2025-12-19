# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Removing a row
df = df.drop(1)

# Printing the DataFrame after removing the row
print("DataFrame after removing row 1:")
print(df)
