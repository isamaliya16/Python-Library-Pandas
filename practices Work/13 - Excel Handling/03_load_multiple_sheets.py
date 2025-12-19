
import pandas as pd

# Load data from multiple sheets in Excel file
df = pd.read_excel('13 - Excel Handling/data/03_multiple_sheets.xlsx', sheet_name=None)
print(df)
    