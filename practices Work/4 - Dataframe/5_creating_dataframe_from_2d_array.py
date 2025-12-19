# creating_dataframe_from_2d_array.py
import pandas as pd
import numpy as np

# Creating a DataFrame from a 2D NumPy array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Display the DataFrame
print("DataFrame created from a 2D NumPy array:")
print(df)
