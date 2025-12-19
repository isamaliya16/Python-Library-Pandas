import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None],
    'C': [1, 2, 3, 4]
})

# Drop columns with any missing data
cleaned_df = df.dropna(axis=1, how='any')

# Display the cleaned DataFrame
print("DataFrame after dropping columns with any missing data:\n", cleaned_df)
