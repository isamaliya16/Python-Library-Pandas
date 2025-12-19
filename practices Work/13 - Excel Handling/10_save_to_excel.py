
import pandas as pd

# Create DataFrame and save to Excel file
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
df.to_excel('13 - Excel Handling/data/10_saved.xlsx', index=False)
print('Data saved to 10_saved.xlsx')
    