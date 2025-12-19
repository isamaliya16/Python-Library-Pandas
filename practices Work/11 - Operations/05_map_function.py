# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Defining a mapping dictionary
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

# Mapping the values of a column using map function
mapped_column = df['A'].map(mapping)

# Printing the mapped column
print("Mapped Column A:")
print(mapped_column)
 
 