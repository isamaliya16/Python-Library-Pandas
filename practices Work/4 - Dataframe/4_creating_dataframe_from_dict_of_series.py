# creating_dataframe_from_dict_of_series.py
import pandas as pd

# Creating a DataFrame from a dictionary of Series
data = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']),
        'Age': pd.Series([25, 30, 35]),
        'City': pd.Series(['New York', 'Los Angeles', 'Chicago'])}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame created from a dictionary of Series:")
print(df) 
