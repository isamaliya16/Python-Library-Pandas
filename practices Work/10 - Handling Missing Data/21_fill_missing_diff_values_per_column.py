import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data with different values per column
filled_df = df.fillna({'A': df['A'].mean(), 'B': df['B'].median()})

# Display the filled DataFrame
print("DataFrame after filling missing data with different values per column:\n", filled_df)
