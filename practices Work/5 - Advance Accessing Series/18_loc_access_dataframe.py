# loc_access_dataframe.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'A': [3, 6, 9],
    'B': [12, 15, 18]
}
df = pd.DataFrame(data)

# Accessing with loc
print(df.loc[1, 'B'])  # Output: 15
