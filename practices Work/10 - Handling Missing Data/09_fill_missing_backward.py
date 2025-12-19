import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data using backward fill
filled_df = df.fillna(method='bfill')

# Display the filled DataFrame
print("DataFrame after backward fill:\n", filled_df)
