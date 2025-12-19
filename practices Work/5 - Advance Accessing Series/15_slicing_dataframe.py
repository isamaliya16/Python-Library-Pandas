# slicing_dataframe.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'A': [100, 200, 300, 400],
    'B': [500, 600, 700, 800]
}
df = pd.DataFrame(data)

# Slicing
print(df[1:3])  # Second and third rows
