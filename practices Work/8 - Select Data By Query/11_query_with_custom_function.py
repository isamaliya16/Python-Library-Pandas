import pandas as pd

# Creating a DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [24, 27, 22, 32]}
df = pd.DataFrame(data)

# Defining a custom function
def is_adult(age):
    return age >= 18

# Using boolean indexing instead of query()
result = df[df['age'].apply(is_adult)]

print(result)
