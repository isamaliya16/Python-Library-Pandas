
import pandas as pd

# Load data from Excel file without header
df = pd.read_excel('13 - Excel Handling/data/19_no_header.xlsx', header=None)
print(df)
    