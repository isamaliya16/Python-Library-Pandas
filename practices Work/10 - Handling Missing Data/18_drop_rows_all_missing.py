import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [None, None, None, 4],
    'B': [None, 2, 3, None]
})

# Drop rows with all missing data
cleaned_df = df.dropna(how='all')

# Display the cleaned DataFrame
print("DataFrame after dropping rows with all missing data:\n", cleaned_df)
