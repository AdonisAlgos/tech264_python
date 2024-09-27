import json

# Create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Convert the dictionary to a JSON-formatted string
json_string = json.dumps(servers_dict, indent=4)

# Print the JSON-formatted string to verify the conversion
print("JSON formatted string:")
print(json_string)

# Convert the dictionary to a JSON file
with open("servers.json", "w") as json_file:  # Open (or create) a file in write mode
    json.dump(servers_dict, json_file, indent=4)  # Write the dictionary to the file in JSON format
    print("\nJSON file 'servers.json' created successfully.")