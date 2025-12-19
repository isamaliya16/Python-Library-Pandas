import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Identify non-missing data using notna()
print("Identify non-missing data using notna():\n", df.notna())
