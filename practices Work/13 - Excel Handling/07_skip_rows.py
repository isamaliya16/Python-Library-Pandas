
import pandas as pd

# Load data from Excel file skipping rows
df = pd.read_excel('13 - Excel Handling/data/07_skip_rows.xlsx', skiprows=2)
print(df)
    