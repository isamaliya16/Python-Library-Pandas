import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data in 'A' with 0 and in 'B' with 5
filled_df = df.fillna({'A': 0, 'B': 5})

# Display the filled DataFrame
print("DataFrame after filling missing data column-wise:\n", filled_df)
