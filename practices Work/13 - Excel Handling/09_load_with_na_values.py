
import pandas as pd

# Load data from Excel file and treat specific values as NA
df = pd.read_excel('13 - Excel Handling/data/09_na_values.xlsx', na_values=['NA', '-'])
print(df)
    