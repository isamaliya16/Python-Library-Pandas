# access_df_row_by_index.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'A': [10, 20, 30],
    'B': [40, 50, 60]
}
df = pd.DataFrame(data)

# Accessing a row by index
print(df.iloc[1])  # Second row
