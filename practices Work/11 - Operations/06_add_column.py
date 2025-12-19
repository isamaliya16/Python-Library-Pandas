# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Adding a new column
df['C'] = df['A'] + df['B']

# Printing the DataFrame with new column
print("DataFrame with new column C:")
print(df)
