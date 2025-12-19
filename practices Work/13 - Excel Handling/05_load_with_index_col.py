
import pandas as pd

# Load data from Excel file with specific column as index
df = pd.read_excel('13 - Excel Handling/data/05_index_col.xlsx', index_col=0)
print(df)
    