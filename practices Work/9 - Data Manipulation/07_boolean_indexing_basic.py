import pandas as pd

# Creating a DataFrame with sample data
data = {'Name': ['Emma', 'Liam', 'Olivia', 'Noah'],
        'Score': [88, 92, 95, 85],
        'Passed': [True, True, True, False]}

df = pd.DataFrame(data)

# Boolean indexing to filter rows where 'Passed' is True
print(df[df['Passed']])
