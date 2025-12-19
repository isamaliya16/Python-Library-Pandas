# conditional_selection_dataframe.py
import pandas as pd

# Creating a Pandas DataFrame
data = {
    'Age': [23, 45, 30, 25],
    'Score': [88, 92, 79, 85]
}
df = pd.DataFrame(data)

# Conditional selection
print(df[df['Age'] > 30])
