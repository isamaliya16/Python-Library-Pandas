import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, np.nan, 5],
    'B': [np.nan, 2, 3, np.nan, np.nan]
})

# Interpolate missing data with limit
interpolated_df = df.interpolate(limit=2)

# Display the interpolated DataFrame
print("DataFrame after interpolation with limit:\n", interpolated_df)
