# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Basic indexing to select a column
col_a = df['A']

# Printing the selected column
print("Column A:")
print(col_a)
