# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Values': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# Grouping by 'Category' and calculating the mean
grouped_mean = df.groupby('Category').mean()

# Printing the grouped mean
print("Mean of values grouped by Category:")
print(grouped_mean)
