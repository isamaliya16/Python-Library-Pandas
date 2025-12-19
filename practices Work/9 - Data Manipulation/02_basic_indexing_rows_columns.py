import pandas as pd

# Creating a DataFrame with sample data
data = {'Product': ['Laptop', 'Tablet', 'Smartphone', 'Printer'],
        'Price': [800, 300, 400, 150],
        'Stock': [10, 20, 30, 40]}

df = pd.DataFrame(data)

# Basic indexing to access rows and columns
print(df.iloc[0, 0])  # First row, first column
print(df.iloc[2, 1])  # Third row, second column

# Accessing rows and columns using loc
print(df.loc[1, 'Product'])  # Second row, 'Product' column
print(df.loc[3, 'Stock'])  # Fourth row, 'Stock' column
