import pandas as pd

# Creating a DataFrame with date column
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Date': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01'])
}

df = pd.DataFrame(data)

# Writing DataFrame to CSV file with date formatting
df.to_csv('output16.csv', index=False, date_format='%Y-%m-%d')
print("Data with dates written to output16.csv")
