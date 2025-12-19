import pandas as pd

# Reading specific columns from CSV file
df = pd.read_csv('12 - CSV Handling/data/data05.csv', usecols=['Name', 'Age'])
print(df)
