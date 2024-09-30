import os
import yaml
import sys

# Ensure the user provides exactly one argument for the folder path
if len(sys.argv) != 2:
    print("Usage: python check_files_valid_yaml.py <folder_path>")
    sys.exit(1)

# Get the folder path from the command-line argument
folder_path = sys.argv[1]

# Check if the provided folder path is valid
if not os.path.isdir(folder_path):
    print("Invalid folder path. Please check and try again.")
    sys.exit(1)

# List all files in the given folder (no recursion into subfolders)
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Skip directories and non-YAML files based on extension
    if os.path.isdir(file_path):
        print(f"Skipping directory: {file_path}")
        continue
    if not (file_name.endswith(".yaml") or file_name.endswith(".yml")):
        print(f"Skipping non-YAML file: {file_path}")
        continue

    # Try to load the YAML file
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"Valid YAML: {file_path}")
    except yaml.YAMLError as exc:
        print(f"Invalid YAML: {file_path}\nError: {exc}")
