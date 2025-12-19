
import pandas as pd

# Create multiple DataFrames and save to Excel file with multiple sheets
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'X': [7, 8, 9], 'Y': [10, 11, 12]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
with pd.ExcelWriter('13 - Excel Handling/data/12_multiple_sheets.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')
print('Data saved to 12_multiple_sheets.xlsx')
    