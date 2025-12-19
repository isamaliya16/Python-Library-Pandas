import pandas as pd

# Creating a DataFrame with sample data
data = {'Product': ['Laptop', 'Tablet', 'Smartphone', 'Printer'],
        'Price': [800, 300, 400, 150],
        'Stock': [10, 20, 5, 15]}

df = pd.DataFrame(data)

# Boolean indexing with combined conditions
print(df[(df['Price'] < 500) & (df['Stock'] > 10)])
