import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing specific columns to CSV file
df[['Name', 'City']].to_csv('12 - CSV Handling/data/output06.csv', index=False)
print("Selected columns written to output06.csv")
