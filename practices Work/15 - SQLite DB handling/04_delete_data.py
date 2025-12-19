# 04_delete_data.py
# This script demonstrates how to delete data from an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Delete data using SQL query
delete_query = """
DELETE FROM employees
WHERE name = 'Charlie';
"""
conn.execute(delete_query)
conn.commit()

# Verify deletion
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)
print(df)

# Close the connection
conn.close()
