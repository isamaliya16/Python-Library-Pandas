import pandas as pd
import json

# Read JSON data from a file
with open('14 - JSON Handling/data/01_basic_index.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.DataFrame([data])

# Display the DataFrame
print(df)

# Write DataFrame to JSON file 
df.to_json('14 - JSON Handling/data/output_01_basic_index.json', orient='records', lines=True)
