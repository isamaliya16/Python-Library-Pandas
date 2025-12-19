import pandas as pd

# Creating a DataFrame with sample data
data = {'Fruit': ['Apple', 'Banana', 'Cherry', 'Date'],
        'Quantity': [5, 10, 15, 20],
        'Price': [1.5, 0.75, 2.0, 3.0]}

df = pd.DataFrame(data)

# Sorting the DataFrame
df_sorted = df.sort_values(by='Price')
print(df_sorted)
