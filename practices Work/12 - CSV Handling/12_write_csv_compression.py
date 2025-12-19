import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to a compressed CSV file
df.to_csv('12 - CSV Handling/data/output12.csv.gz', index=False, compression='gzip')
print("Data written to compressed file output12.csv.gz")
