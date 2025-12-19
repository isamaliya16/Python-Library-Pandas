# 09_export_to_csv.py
# This script demonstrates how to export data from an SQLite database table to a CSV file using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Reading data from the table
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)

# Export data to CSV
df.to_csv('15 - SQLite DB Handling/data/employees.csv', index=False)

# Close the connection
conn.close()
