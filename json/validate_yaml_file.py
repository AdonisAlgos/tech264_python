import os
import sys
import yaml

if len(sys.argv) > 1:
    # check file exists
    if os.path.exists(sys.argv[1]):
        # open file for reading - parse the YAML file - if it loads then the file contains valid YAML
        with open(sys.argv[1], "r") as yaml_file:
            yaml.safe_load(yaml_file)
            print("YAML file is valid!")
    else:
        # alert user that file specified does not exist
        print("ERROR: File '" + sys.argv[1] + "' not found")
else:
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")