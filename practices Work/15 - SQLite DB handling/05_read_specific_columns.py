# 05_read_specific_columns.py
# This script demonstrates how to read specific columns from an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Reading specific columns
query = "SELECT name, department FROM employees"
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
