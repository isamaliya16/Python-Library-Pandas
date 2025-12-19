# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Values': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# Grouping by 'Category' and summing the values
grouped_sum = df.groupby('Category').sum()

# Printing the grouped sum
print("Sum of values grouped by Category:")
print(grouped_sum)
