import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# Interpolate missing data using different methods
linear_interpolated_df = df.interpolate(method='linear')
polynomial_interpolated_df = df.interpolate(method='polynomial', order=2)

# Display the interpolated DataFrame
print("DataFrame after linear interpolation:\n", linear_interpolated_df)
print("DataFrame after polynomial interpolation:\n", polynomial_interpolated_df)
