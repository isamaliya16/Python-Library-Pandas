# 08_join_tables.py
# This script demonstrates how to join two tables in an SQLite database using Pandas.

import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('15 - SQLite DB Handling/data/example.db')

# SQL query to create a second table
create_table_query = """
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
);
"""
conn.execute(create_table_query)
conn.commit()

# Insert data into the second table
data = {
    'department_id': [1, 2, 3],
    'department_name': ['HR', 'Engineering', 'Sales']
}
df_departments = pd.DataFrame(data)
df_departments.to_sql('departments', conn, if_exists='append', index=False)

# Join tables using SQL query
query = """
SELECT e.name, e.age, d.department_name
FROM employees e
JOIN departments d ON e.department = d.department_name
"""
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
