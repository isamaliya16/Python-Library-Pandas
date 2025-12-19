import pandas as pd

# Reading CSV file with a different delimiter
df = pd.read_csv('12 - CSV Handling/data/data09.csv', delimiter=';')
print(df)
