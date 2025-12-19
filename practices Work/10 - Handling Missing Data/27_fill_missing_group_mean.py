import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Values': [1, None, 3, None]
})

# Fill missing data with group-based mean
df['Values'] = df.groupby('Category')['Values'].transform(lambda x: x.fillna(x.mean()))

# Display the filled DataFrame
print("DataFrame after filling missing data with group-based mean:\n", df)
