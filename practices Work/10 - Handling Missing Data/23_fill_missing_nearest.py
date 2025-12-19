import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, None, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data with nearest value
filled_df = df.interpolate(method='nearest')

# Display the filled DataFrame
print("DataFrame after filling missing data with nearest value:\n", filled_df)
