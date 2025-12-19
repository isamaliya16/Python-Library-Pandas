# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# Calculating descriptive statistics
summary = df.describe()

# Printing the summary statistics
print("Summary statistics of DataFrame:")
print(summary)
