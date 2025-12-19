import pandas as pd

# Reading CSV file with custom column names
df = pd.read_csv('data17.csv', names=['ID', 'Name', 'Age', 'City'])
print(df)
