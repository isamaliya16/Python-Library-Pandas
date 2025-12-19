import pandas as pd

# Reading CSV file with custom index column
df = pd.read_csv('12 - CSV Handling/data/data03.csv', index_col='ID')
print(df)
