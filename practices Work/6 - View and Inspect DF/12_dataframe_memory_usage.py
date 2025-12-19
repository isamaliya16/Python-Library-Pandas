# 12_dataframe_memory_usage.py
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Is_Employed': [True, False, True, True]}
df = pd.DataFrame(data)

# Viewing memory usage
print(df.memory_usage())
