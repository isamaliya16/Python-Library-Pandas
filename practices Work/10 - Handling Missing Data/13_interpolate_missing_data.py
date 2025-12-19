import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Interpolate missing data
interpolated_df = df.interpolate()

# Display the interpolated DataFrame
print("DataFrame after interpolating missing data:\n", interpolated_df)
