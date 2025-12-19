import pandas as pd

# Reading CSV file and skipping rows
df = pd.read_csv('12 - CSV Handling/data/data19.csv', skiprows=2)
print(df)
