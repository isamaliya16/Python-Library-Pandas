import pandas as pd

# Reading CSV file and handling missing values
df = pd.read_csv('12 - CSV Handling/data/data07.csv', na_values=['NA', 'Unknown'])
print(df)
