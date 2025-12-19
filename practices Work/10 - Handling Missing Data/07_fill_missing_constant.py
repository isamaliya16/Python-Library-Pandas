import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Fill missing data with a constant value
filled_df = df.fillna(0)

# Display the filled DataFrame
print("DataFrame after filling missing data with 0:\n", filled_df)
