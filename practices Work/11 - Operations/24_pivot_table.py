# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Type': ['X', 'Y', 'X', 'Y'], 'Values': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# Creating a pivot table
pivot = df.pivot_table(values='Values', index='Category', columns='Type', aggfunc='sum')

# Printing the pivot table
print("Pivot Table:")
print(pivot)
