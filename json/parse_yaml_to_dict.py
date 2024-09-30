# Parsing/converting YAML to a dictionary
import sys
import yaml

with open(sys.argv[1], 'r') as yaml_file:
    dict_data = yaml.safe_load(yaml_file)
    print("YAML file converted successfully")
    print(dict_data)