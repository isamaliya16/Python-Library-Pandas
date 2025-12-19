# Importing pandas library
import pandas as pd

# Creating a DataFrame with duplicated rows
data = {'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6]}
df = pd.DataFrame(data)

# Identifying duplicated rows
duplicated = df.duplicated()

# Printing duplicated rows
print("Duplicated rows in DataFrame:")
print(duplicated)
