# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Type': ['X', 'Y', 'X', 'Y'], 'Values': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# Creating a crosstab
crosstab = pd.crosstab(df['Category'], df['Type'], values=df['Values'], aggfunc='sum')

# Printing the crosstab
print("Crosstab of Category and Type:")
print(crosstab)
