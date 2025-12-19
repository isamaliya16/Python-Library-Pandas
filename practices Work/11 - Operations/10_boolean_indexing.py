# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Using boolean indexing to filter data
filtered_df = df[df['A'] > 2]

# Printing the filtered DataFrame
print("Filtered DataFrame where A > 2:")
print(filtered_df)
