import pandas as pd

# Creating a DataFrame with sample data
data = {'Employee': ['John', 'Jane', 'Jim', 'Jill'],
        'Department': ['HR', 'Finance', 'IT', 'Marketing'],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Boolean indexing using isin
departments = ['Finance', 'IT']
print(df[df['Department'].isin(departments)])
