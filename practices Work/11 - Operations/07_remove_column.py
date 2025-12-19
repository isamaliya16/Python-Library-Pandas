# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Removing a column
df = df.drop('B', axis=1)

# Printing the DataFrame after removing the column
print("DataFrame after removing column B:")
print(df)
