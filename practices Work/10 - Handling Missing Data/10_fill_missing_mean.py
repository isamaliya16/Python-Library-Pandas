import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data with mean value of each column
filled_df = df.fillna(df.mean())

# Display the filled DataFrame
print("DataFrame after filling missing data with mean:\n", filled_df)
