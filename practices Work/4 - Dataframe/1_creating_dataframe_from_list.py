# creating_dataframe_from_list.py
import pandas as pd

# Creating a DataFrame from a list
data = [10, 20, 30, 40, 50]
df = pd.DataFrame(data, columns=['Numbers'])

# Display the DataFrame
print("DataFrame created from a list:")
print(df)