import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Drop columns with more than 2 missing data
cleaned_df = df.dropna(axis=1, thresh=3)

# Display the cleaned DataFrame
print("DataFrame after dropping columns with more than 2 missing data:\n", cleaned_df)
