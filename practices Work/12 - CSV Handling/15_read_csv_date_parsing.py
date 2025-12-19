import pandas as pd

# Reading CSV file and parsing dates
df = pd.read_csv('12 - CSV Handling/data/data15.csv', parse_dates=['Date'])
print(df)
