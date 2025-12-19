# 06_filter_data.py
# This script demonstrates how to filter data from an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Filter data using SQL query
query = "SELECT * FROM employees WHERE age > 25"
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
