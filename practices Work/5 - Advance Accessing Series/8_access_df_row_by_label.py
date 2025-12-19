# access_df_row_by_label.py
import pandas as pd

# Creating a Pandas DataFrame with custom index
data = {
    'P': [15, 25, 35],
    'Q': [45, 55, 65]
}
df = pd.DataFrame(data, index=['x', 'y', 'z'])

# Accessing a row by label
print(df.loc['y'])  # Row with index 'y'
