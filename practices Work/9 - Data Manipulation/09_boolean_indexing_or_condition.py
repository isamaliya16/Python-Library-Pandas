import pandas as pd

# Creating a DataFrame with sample data
data = {'Car': ['Toyota', 'Honda', 'Ford', 'Tesla'],
        'Year': [2015, 2018, 2012, 2020],
        'Electric': [False, False, False, True]}

df = pd.DataFrame(data)

# Boolean indexing with OR condition
print(df[(df['Year'] > 2015) | (df['Electric'])])
