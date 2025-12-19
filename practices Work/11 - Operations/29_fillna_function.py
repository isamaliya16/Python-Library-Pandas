# Importing pandas library
import pandas as pd

# Creating a DataFrame with missing values
data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]}
df = pd.DataFrame(data)

# Filling missing values with a specified value
filled_df = df.fillna(0)

# Printing the DataFrame after filling missing values
print("DataFrame after filling missing values with 0:")
print(filled_df)
