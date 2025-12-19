# access_df_single_column.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'X': [1, 2, 3],
    'Y': [4, 5, 6],
    'Z': [7, 8, 9]
}
df = pd.DataFrame(data)

# Accessing a single column
print(df['X'])
