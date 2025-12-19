import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Identify missing data using isna()
print("Identify missing data using isna():\n", df.isna())
