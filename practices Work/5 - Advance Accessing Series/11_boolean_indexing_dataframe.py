# boolean_indexing_dataframe.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)

# Boolean indexing
print(df[df['Score'] > 90])
