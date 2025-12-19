import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to a CSV file with specific encoding
df.to_csv('12 - CSV Handling/data/output14.csv', index=False, encoding='utf-8')
print("Data written to output14.csv with UTF-8 encoding")
