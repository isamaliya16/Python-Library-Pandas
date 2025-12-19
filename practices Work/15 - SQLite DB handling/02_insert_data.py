# 02_insert_data.py
# This script demonstrates how to insert data into an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Data to be inserted
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [24, 30, 22],
    'department': ['HR', 'Engineering', 'Sales']
}
df = pd.DataFrame(data)

# Insert data into the table
df.to_sql('employees', conn, if_exists='append', index=False)

# Verify insertion
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)
print(df)

# Close the connection
conn.close()
