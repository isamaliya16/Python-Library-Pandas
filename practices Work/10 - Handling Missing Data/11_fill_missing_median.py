import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data with median value of each column
filled_df = df.fillna(df.median())

# Display the filled DataFrame
print("DataFrame after filling missing data with median:\n", filled_df)
