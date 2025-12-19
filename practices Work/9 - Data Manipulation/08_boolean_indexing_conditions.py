import pandas as pd

# Creating a DataFrame with sample data
data = {'Item': ['Apple', 'Banana', 'Cherry', 'Date'],
        'Price': [1.2, 0.5, 2.5, 3.0],
        'Quantity': [10, 20, 15, 5]}

df = pd.DataFrame(data)

# Boolean indexing with multiple conditions
print(df[(df['Price'] < 2) & (df['Quantity'] > 10)])
