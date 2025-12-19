import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, 1],
    'B': [None, 2, 3, None, 3]
})

print(df)

# Fill missing data with mode value of each column
filled_df = df.fillna(df.mode().iloc[0])

# Display the filled DataFrame
print("DataFrame after filling missing data with mode:\n", filled_df)
