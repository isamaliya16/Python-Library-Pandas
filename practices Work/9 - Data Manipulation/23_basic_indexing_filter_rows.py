import pandas as pd

# Creating a DataFrame with sample data
data = {'Country': ['USA', 'Canada', 'Mexico', 'Brazil'],
        'Capital': ['Washington, D.C.', 'Ottawa', 'Mexico City', 'Brasília'],
        'Population': [331, 38, 128, 213]}

df = pd.DataFrame(data)

# Filtering rows
print(df[df['Population'] > 100])
