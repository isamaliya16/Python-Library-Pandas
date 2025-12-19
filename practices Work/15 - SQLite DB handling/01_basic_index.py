# 01_basic_index.py
# This script demonstrates the basic connection to an SQLite database and reading data from a table.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT
);
"""
conn.execute(create_table_query)
conn.commit()

# Reading data from the table
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
