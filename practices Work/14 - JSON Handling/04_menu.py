import pandas as pd
import json

# Read JSON data from a file
with open('14 - JSON Handling/data/04_menu.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.json_normalize(
    data,
    record_path=['menu', 'popup', 'menuitem'],
    meta=[['menu', 'id'], ['menu', 'value']],
    errors='ignore'
)

# Display the DataFrame
print(df)

# Write DataFrame to JSON file
df.to_json('14 - JSON Handling/data/output_04_menu.json', orient='records', lines=True)