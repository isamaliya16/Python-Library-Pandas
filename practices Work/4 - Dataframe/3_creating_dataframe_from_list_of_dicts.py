# creating_dataframe_from_list_of_dicts.py
import pandas as pd

# Creating a DataFrame from a list of dictionaries
data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}]
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame created from a list of dictionaries:")
print(df)
