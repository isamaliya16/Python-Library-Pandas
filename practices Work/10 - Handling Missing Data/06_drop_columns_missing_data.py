import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Drop columns with missing data
cleaned_df = df.dropna(axis=1)

# Display the cleaned DataFrame
print("DataFrame after dropping columns with missing data:\n", cleaned_df)
