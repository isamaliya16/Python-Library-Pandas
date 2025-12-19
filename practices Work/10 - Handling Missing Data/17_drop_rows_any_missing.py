import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, None, None, 4],
    'B': [None, 2, 3, None]
})

# Drop rows with any missing data
cleaned_df = df.dropna(how='any')

# Display the cleaned DataFrame
print("DataFrame after dropping rows with any missing data:\n", cleaned_df)
