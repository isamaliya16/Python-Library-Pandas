# 03_update_data.py
# This script demonstrates how to update data in an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Update data using SQL query
update_query = """
UPDATE employees
SET age = 25
WHERE name = 'Alice';
"""
conn.execute(update_query)
conn.commit()

# Verify update
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)
print(df)

# Close the connection
conn.close()
