#install package to access excel
# ! pip install openpyxl
# ------------------------------------------------

# creating_dataframe_from_excel.py
import pandas as pd

# Creating a DataFrame by reading an Excel file
# (Assuming 'data.xlsx' is present in the same directory)
file_path = '4 - Dataframe/data.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the DataFrame
print("DataFrame created from an Excel file:")
print(df)
