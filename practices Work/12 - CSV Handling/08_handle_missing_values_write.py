import pandas as pd

# Creating a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', None],
    'Age': [24, None, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to CSV file, handling missing values
df.to_csv('12 - CSV Handling/data/output08.csv', index=False, na_rep='Missing')
print("Data with missing values written to output08.csv")
