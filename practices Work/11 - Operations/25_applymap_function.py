# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Defining a function to apply to each element
def add_one(x):
    return x + 1

# Applying the function to each element using applymap
modified_df = df.applymap(add_one)

# Printing the modified DataFrame
print("Modified DataFrame using applymap:")
print(modified_df)
