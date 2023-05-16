import csv
import yaml
import sys
import re

# Get input and output filenames from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the CSV file and store the values in a list of dictionaries
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    csv_data = list(reader)

# Define an empty list to store the new YAML data
yaml_data = []

# Define the pattern for non-alphanumeric characters
pattern = re.compile(r'\W+')

# Iterate through the CSV data and convert it into the desired YAML format
for row in csv_data:
    # Replace non-alphanumeric characters with an empty string
    words = pattern.sub(' ', row['act']).split()
    if len(words) == 1:
        cleaned_act = words[0].lower()
    else:
        cleaned_act = ''.join(word[0].lower() for word in words)
    yaml_data.append({
        'trigger': f":{cleaned_act}",
        'replace': row['prompt']
    })

yaml_data = {'matches': yaml_data}

# Write the new YAML data to the output file
with open(output_file, 'w') as f:
    yaml.dump(yaml_data, f, default_flow_style=False)

