import pandas as pd

# Creating a DataFrame with sample data
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        'Temperature': [85, 75, 60, 90]}

df = pd.DataFrame(data)

# Boolean indexing with string methods
print(df[df['City'].str.contains('New')])
