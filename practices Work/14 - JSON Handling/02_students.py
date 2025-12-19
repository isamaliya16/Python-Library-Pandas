import pandas as pd
import json

# Read JSON data from a file
with open('14 - JSON Handling/data/02_students.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.DataFrame(data['students'])

# Display the DataFrame
print(df)

# Write DataFrame to JSON file
df.to_json('14 - JSON Handling/data/output_02_students.json', orient='records', lines=True)
