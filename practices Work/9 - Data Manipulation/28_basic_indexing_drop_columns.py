import pandas as pd

# Creating a DataFrame with sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Dropping a column
df_dropped = df.drop(columns=['Age'])
print(df_dropped)
