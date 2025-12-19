
import pandas as pd

# Load data from Excel file with custom NA values
df = pd.read_excel('13 - Excel Handling/data/16_custom_na_values.xlsx', na_values=['missing'])
print(df)
    