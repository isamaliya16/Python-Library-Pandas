import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data conditionally
df['A'] = df['A'].fillna(df['A'].mean())
df['B'] = df['B'].fillna(0)

# Display the filled DataFrame
print("DataFrame after conditional filling of missing data:\n", df)
