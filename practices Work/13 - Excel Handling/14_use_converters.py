
import pandas as pd

# Load data from Excel file with converters
df = pd.read_excel('13 - Excel Handling/data/14_converters.xlsx', converters={'A': str})
print(df)
    