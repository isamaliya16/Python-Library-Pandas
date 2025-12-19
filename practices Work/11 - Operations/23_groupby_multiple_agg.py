# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Values': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# Grouping by 'Category' and applying multiple aggregations
grouped_agg = df.groupby('Category').agg(['sum', 'mean'])

# Printing the grouped aggregations
print("Aggregations (sum and mean) of values grouped by Category:")
print(grouped_agg)
