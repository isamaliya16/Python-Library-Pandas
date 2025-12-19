import pandas as pd

# Creating a DataFrame with sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, None, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Boolean indexing with isnull
print(df[df['Age'].isnull()])
