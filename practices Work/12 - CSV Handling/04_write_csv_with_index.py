import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data, index=['A', 'B', 'C'])

# Writing DataFrame to CSV file with index
df.to_csv('12 - CSV Handling/data/output04.csv')
print("Data written to output04.csv with index")
