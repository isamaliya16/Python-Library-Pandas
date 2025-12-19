
import pandas as pd

# Load data from Excel file as Series
series = pd.read_excel('13 - Excel Handling/data/20_squeeze.xlsx', squeeze=True)
print(series)
    