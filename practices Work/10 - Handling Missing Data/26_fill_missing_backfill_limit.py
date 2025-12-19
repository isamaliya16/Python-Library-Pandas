import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, np.nan, np.nan, 4, 5],
    'B': [np.nan, 2, np.nan, 4, np.nan]
})

# Fill missing data with backfill and limit
filled_df = df.fillna(method='bfill', limit=2)

# Display the filled DataFrame
print("DataFrame after backfill with limit:\n", filled_df)
