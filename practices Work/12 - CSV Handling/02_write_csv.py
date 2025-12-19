import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to CSV file
df.to_csv('12 - CSV Handling/data/output02.csv', index=False)
print("Data written to output02.csv")
