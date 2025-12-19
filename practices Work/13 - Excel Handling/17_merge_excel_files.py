
import pandas as pd

# Load and merge data from multiple Excel files
df1 = pd.read_excel('13 - Excel Handling/data/17_file1.xlsx')
df2 = pd.read_excel('13 - Excel Handling/data/17_file2.xlsx')
merged_df = pd.concat([df1, df2])
print(merged_df)
    