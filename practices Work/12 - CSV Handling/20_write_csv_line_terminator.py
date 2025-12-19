import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Writing DataFrame to CSV file with custom line terminator
df.to_csv('12 CSV Handling/data/output20.csv', index=False, line_terminator='\r\n')
print("Data written to output20.csv with custom line terminator")
