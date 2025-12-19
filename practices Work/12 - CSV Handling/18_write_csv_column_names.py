import pandas as pd

# Creating a DataFrame
data = {
    'ID' : [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to CSV file with custom column names
df.to_csv('output18.csv', header=['ID', 'Name', 'Age', 'City'], index=False)
print("Data written to output18.csv with custom column names")
