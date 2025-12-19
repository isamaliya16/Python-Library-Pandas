import pandas as pd

# Creating a DataFrame with sample data
data = {'Fruit': ['Apple', 'Banana', 'Cherry', 'Date'],
        'Quantity': [5, 10, 15, 20],
        'Price': [1.5, 0.75, 2.0, 3.0]}

df = pd.DataFrame(data)

# Setting values using loc
df.loc[1, 'Price'] = 0.80
print(df)
