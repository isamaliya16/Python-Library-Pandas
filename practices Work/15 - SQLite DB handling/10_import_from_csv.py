# 10_import_from_csv.py
# This script demonstrates how to import data from a CSV file into an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Import data from CSV
df = pd.read_csv('15 - SQLite DB Handling/data/new_employees.csv')

# Insert data into the table
df.to_sql('employees', conn, if_exists='append', index=False)

# Verify insertion
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)
print(df)

# Close the connection
conn.close()
