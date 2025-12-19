import pandas as pd

# Creating a DataFrame with sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Basic indexing to access a single column
print(df['Name'])

# Basic indexing to access multiple columns
print(df[['Name', 'City']])

# Accessing rows using iloc
print(df.iloc[0])  # First row
print(df.iloc[1:3])  # Second and third row
