import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [None, None, None, None],
    'B': [None, 2, 3, None],
    'C': [1, 2, 3, 4]
})

# Drop columns with all missing data
cleaned_df = df.dropna(axis=1, how='all')

# Display the cleaned DataFrame
print("DataFrame after dropping columns with all missing data:\n", cleaned_df)
