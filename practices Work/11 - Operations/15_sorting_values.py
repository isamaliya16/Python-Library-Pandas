# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [3, 2, 1], 'B': [6, 5, 4]}
df = pd.DataFrame(data)

# Sorting the DataFrame by column 'A'
sorted_df = df.sort_values(by='A')

# Printing the sorted DataFrame
print("DataFrame sorted by column A:")
print(sorted_df)
