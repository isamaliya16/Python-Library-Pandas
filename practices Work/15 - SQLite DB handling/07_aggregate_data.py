# 07_aggregate_data.py
# This script demonstrates how to perform aggregate functions on data in an SQLite database table using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# Aggregate data using SQL query
query = """
SELECT department, COUNT(*) as count, AVG(age) as average_age
FROM employees
GROUP BY department
"""
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
