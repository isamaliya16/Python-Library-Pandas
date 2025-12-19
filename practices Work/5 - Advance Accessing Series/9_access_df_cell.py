# access_df_cell.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'A': [5, 10, 15],
    'B': [20, 25, 30]
}
df = pd.DataFrame(data)

# Accessing a single cell
print(df.at[1, 'B'])  # Cell at second row and column 'B'
