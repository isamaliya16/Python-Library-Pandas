import pandas as pd

# Creating a DataFrame with sample data
data = {'Country': ['USA', 'Canada', 'Mexico', 'Brazil'],
        'Capital': ['Washington, D.C.', 'Ottawa', 'Mexico City', 'Brasília'],
        'Population': [331, 38, 128, 213]}

df = pd.DataFrame(data)

# Indexing using iloc
print(df.iloc[0])  # First row
print(df.iloc[1:3])  # Rows 1 to 2 inclusive
print(df.iloc[:, 0])  # All rows, first column
print(df.iloc[1:3, 0:2])  # Rows 1 to 2, first two columns
