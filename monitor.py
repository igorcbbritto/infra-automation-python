import subprocess
import json

def ping_server(ip):
    result = subprocess.run(["ping", "-n", "1", ip], capture_output=True)
    return result.returncode == 0

with open("servers.json", "r", encoding="utf-8") as file:
    servers = json.load(file)

for server in servers:
    status = ping_server(server["ip"])

    if status:
        print(f"{server['name']} ONLINE")
    else:
        print(f"{server['name']} OFFLINE")
