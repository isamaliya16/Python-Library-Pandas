import pandas as pd
import json

# Read JSON data from a file
with open('14 - JSON Handling/data/03_company.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.json_normalize(data, 'employees', ['company', 'location'])

# Display the DataFrame
print(df) 

# Write DataFrame to JSON file
df.to_json('14 - JSON Handling/data/output_03_company.json', orient='records', lines=True)
