# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Applying a lambda function to a column
df['C'] = df['A'].apply(lambda x: x * 2)

# Printing the DataFrame with new column
print("DataFrame with column C using apply and lambda:")
print(df)
