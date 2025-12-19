# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 2, 3], 'B': [4, 4, 5, 6]}
df = pd.DataFrame(data)

# Counting unique values in column 'A'
value_counts = df['A'].value_counts()

# Printing the value counts
print("Value counts in column A:")
print(value_counts)
