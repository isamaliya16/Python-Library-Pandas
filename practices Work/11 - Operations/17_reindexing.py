# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Reindexing the DataFrame
reindexed_df = df.reindex([2, 0, 1])

# Printing the reindexed DataFrame
print("Reindexed DataFrame:")
print(reindexed_df)
