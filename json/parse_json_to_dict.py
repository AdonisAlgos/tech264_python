import json

# Read the existing JSON file and convert it to a Python dictionary
with open('servers.json', 'r') as json_file:
    servers = json.load(json_file)

print(servers)

# Loop through the main dictionary
for server_key, server_info in servers.items():
    # Print the key and the entire sub-dictionary as a string
    print(f"Key and value: '{server_key}' = '{server_info}'")

    # Loop through the sub-dictionary and print each key-value pair
    for info_key, info_value in server_info.items():
        print(f"Record key and sub value: '{info_key}' = '{info_value}'")
