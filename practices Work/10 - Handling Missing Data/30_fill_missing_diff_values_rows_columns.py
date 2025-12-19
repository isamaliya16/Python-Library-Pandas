import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, np.nan]
})

# Fill missing data in different rows and columns
filled_df = df.apply(lambda x: x.fillna({0: 0, 1: x.mean(), 2: x.median(), 3: 10}[x.name] if pd.isna(x.mean()) else x.fillna(x.mean())))

# Display the filled DataFrame
print("DataFrame after filling missing data with different values for rows and columns:\n", filled_df)

