# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2], 'B': [4, 5]}
df = pd.DataFrame(data)

# Adding a new row
new_row = pd.DataFrame({'A': [3], 'B': [6]})
df = pd.concat([df, new_row], ignore_index=True)

# Printing the DataFrame with new row
print("DataFrame with new row:")
print(df)
