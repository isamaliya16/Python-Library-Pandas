
import pandas as pd

# Load data from Excel file with custom header
df = pd.read_excel('13 - Excel Handling/data/18_header.xlsx', header=1)
print(df)
    