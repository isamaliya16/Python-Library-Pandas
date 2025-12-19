import pandas as pd
import numpy as np

# Create a DataFrame with time series data
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, np.nan, 6],
    'B': [np.nan, 2, 3, np.nan, 5, np.nan]
}, index=dates)

# Fill missing data with forward fill
filled_df = df.fillna(method='ffill')

# Display the filled DataFrame
print("DataFrame after forward fill in time series:\n", filled_df)
