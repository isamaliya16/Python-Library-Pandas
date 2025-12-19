import pandas as pd

# Creating a DataFrame with sample data
data = {'Fruit': ['Apple', 'Banana', 'Cherry', 'Date'],
        'Quantity': [5, 10, 15, 20],
        'Price': [1.5, 0.75, 2.0, 3.0]}

df = pd.DataFrame(data)

# Indexing using loc
print(df.loc[0])  # First row
print(df.loc[1:3])  # Rows 1 to 3 inclusive
print(df.loc[:, 'Fruit'])  # All rows, 'Fruit' column
print(df.loc[1:3, 'Fruit':'Quantity'])  # Rows 1 to 3, 'Fruit' to 'Quantity' columns
