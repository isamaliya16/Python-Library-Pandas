import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, np.nan]
})

# Drop rows with more than 1 missing data
cleaned_df = df.dropna(thresh=2)

# Display the cleaned DataFrame
print("DataFrame after dropping rows with more than 1 missing data:\n", cleaned_df)
