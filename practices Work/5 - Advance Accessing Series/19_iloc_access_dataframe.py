# iloc_access_dataframe.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'X': [7, 14, 21],
    'Y': [28, 35, 42]
}
df = pd.DataFrame(data)

# Accessing with iloc
print(df.iloc[2, 0])  # Output: 21
