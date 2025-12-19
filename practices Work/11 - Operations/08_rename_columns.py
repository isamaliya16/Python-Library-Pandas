# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Renaming columns
df = df.rename(columns={'A': 'Alpha', 'B': 'Beta'})

# Printing the DataFrame with renamed columns
print("DataFrame with renamed columns:")
print(df)
