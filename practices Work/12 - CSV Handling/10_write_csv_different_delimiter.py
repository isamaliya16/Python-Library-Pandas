import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to CSV file with a different delimiter
df.to_csv('12 - CSV Handling/data/output10.csv', sep=';', index=False)
print("Data written to output10.csv with semicolon delimiter")
