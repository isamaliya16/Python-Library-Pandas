# Importing pandas library
import pandas as pd

# Creating a simple DataFrame with index
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data, index=['c', 'a', 'b'])

# Sorting the DataFrame by index
sorted_df = df.sort_index()

# Printing the sorted DataFrame by index
print("DataFrame sorted by index:")
print(sorted_df)
