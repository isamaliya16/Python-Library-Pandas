import pandas as pd

# Creating a DataFrame with sample data
data = {'Name': ['Emma', 'Liam', 'Olivia', 'Noah'],
        'Score': [88, None, 95, 85]}

df = pd.DataFrame(data)

# Boolean indexing with notnull
print(df[df['Score'].notnull()])
