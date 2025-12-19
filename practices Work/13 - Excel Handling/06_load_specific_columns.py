
import pandas as pd

# Load specific columns from Excel file
df = pd.read_excel('13 - Excel Handling/data/06_specific_columns.xlsx', usecols=['A', 'B'])
print(df)
    