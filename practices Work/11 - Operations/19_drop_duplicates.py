# Importing pandas library
import pandas as pd

# Creating a DataFrame with duplicated rows
data = {'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6]}
df = pd.DataFrame(data)

# Dropping duplicated rows
df_no_duplicates = df.drop_duplicates()

# Printing DataFrame after dropping duplicates
print("DataFrame after dropping duplicates:")
print(df_no_duplicates)
