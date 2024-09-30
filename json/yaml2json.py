import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml2json.py <source_file.yaml> <target_file.json>")

# 1. Convert the YAML to JSON

# Open the YAML file and convert to python dictionary
with open(sys.argv[1],"r") as yaml_file:
    data_dict = yaml.safe_load(yaml_file)

# Serialise Python dictionary to JSON-formatted string
json_data = json.dumps(data_dict, indent=4)


# 2. Save the JSON into a new file with the name for it received as a argument
# 2.1 Check the target file name was specified as an argument, if not, output the JSON to the screen instead
if not len(sys.argv) > 2:
    print(json_data)
    sys.exit(1)

# 2.2 Check the target file doesn't already exist
if os.path.exists(sys.argv[2]):
        print(f"Error: The file '{sys.argv[2]}' already exists. Please choose a different file name.")

# 2.3 If previous conditions not met, then save JSON file
else:
    with open(sys.argv[2], 'w') as json_file:
        json_file.write(json_data)