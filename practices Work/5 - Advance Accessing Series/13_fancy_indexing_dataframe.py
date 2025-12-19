# fancy_indexing_dataframe.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Fancy indexing
print(df.iloc[[0, 2]])  # First and third rows
