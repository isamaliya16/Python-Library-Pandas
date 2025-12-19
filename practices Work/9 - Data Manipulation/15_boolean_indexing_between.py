import pandas as pd

# Creating a DataFrame with sample data
data = {'Product': ['Laptop', 'Tablet', 'Smartphone', 'Printer'],
        'Price': [800, 300, 400, 150]}

df = pd.DataFrame(data)

# Boolean indexing with between
print(df[df['Price'].between(200, 500)])
