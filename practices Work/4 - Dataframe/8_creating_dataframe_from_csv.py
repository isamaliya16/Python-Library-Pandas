# creating_dataframe_from_csv.py
import pandas as pd

# Creating a DataFrame by reading a CSV file
# (Assuming 'data.csv' is present in the same directory)
file_path = '4 - Dataframe/data.csv'
df = pd.read_csv(file_path)

# Display the DataFrame
print("DataFrame created from a CSV file:")
print(df)
