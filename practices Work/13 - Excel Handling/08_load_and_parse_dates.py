
import pandas as pd

# Load data from Excel file and parse dates
df = pd.read_excel('13 - Excel Handling/data/08_parse_dates.xlsx', parse_dates=['Date'])
print(df)
    