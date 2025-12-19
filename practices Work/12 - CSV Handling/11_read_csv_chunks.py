import pandas as pd

# Reading a large CSV file in chunks
chunk_size = 2
for chunk in pd.read_csv('12 - CSV Handling/data/data11.csv', chunksize=chunk_size):
    print(chunk)
