import pandas as pd

# Custom function to fill missing data
def fill_custom(value):
    if pd.isna(value):
        return 0
    return value

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Apply custom function to fill missing data
filled_df = df.applymap(fill_custom)

# Display the filled DataFrame
print("DataFrame after filling missing data with custom function:\n", filled_df)
