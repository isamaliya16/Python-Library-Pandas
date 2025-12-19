#install package to access excel
# ! pip install openpyxl
# ------------------------------------------------

import pandas as pd

# Load data from Excel file
df = pd.read_excel('13 - Excel Handling/data/01_basic_index.xlsx')
print(df)
    