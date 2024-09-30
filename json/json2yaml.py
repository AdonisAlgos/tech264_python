import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library
# Open the JSON file and read its contents
with open(sys.argv[1], "r") as json_file:
    dict_data = json.load(json_file)

# Serialise python dictionary to YAML-formatted string
yaml_data = yaml.dump(dict_data)

# 2. Save the YAML into a new file with the name for it received as a argument
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
if not len(sys.argv) > 2:
    print(yaml_data)
    sys.exit(1)

# 2.2 Check the target file doesn't already exist
if os.path.exists(sys.argv[2]):
        print(f"Error: The file '{sys.argv[2]}' already exists. Please choose a different file name.")

# 2.3 If previous conditions not met, then save YAML file
else:
    with open(sys.argv[2], 'w') as yaml_file:
        yaml_file.write(yaml_data)
