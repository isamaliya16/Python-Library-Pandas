# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Replacing specific values in the DataFrame
replaced_df = df.replace({1: 'one', 5: 'five'})

# Printing the DataFrame after replacing values
print("DataFrame after replacing values:")
print(replaced_df)
