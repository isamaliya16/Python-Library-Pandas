
import pandas as pd

# Load data from specific sheet in Excel file
df = pd.read_excel('13 - Excel Handling/data/04_specific_sheet.xlsx', sheet_name='Sheet1')
print(df)
    