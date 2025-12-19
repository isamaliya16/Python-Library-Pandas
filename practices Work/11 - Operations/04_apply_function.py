# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Defining a function to apply
def square(x):
    return x ** 2

# Applying the function to each element of DataFrame
squared_df = df.applymap(square)

# Printing the squared DataFrame
print("Squared DataFrame:")
print(squared_df)
