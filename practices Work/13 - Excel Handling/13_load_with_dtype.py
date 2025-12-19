
import pandas as pd

# Load data from Excel file with specific data types
df = pd.read_excel('13 - Excel Handling/data/13_dtype.xlsx', dtype={'A': int, 'B': float})
print(df)
    