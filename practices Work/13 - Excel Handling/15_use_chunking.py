
import pandas as pd

# Load data from Excel file in chunks
chunks = pd.read_excel('13 - Excel Handling/data/15_chunking.xlsx', chunksize=2)
for chunk in chunks:
    print(chunk)
    