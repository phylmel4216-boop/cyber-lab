import socket
import os

os.makedirs("data", exist_ok=True)

hostname = socket.gethostname()

try:
    ip = socket.gethostbyname(hostname)
except socket.error:
    ip = "Unavailable"

result = (
    "===== CYBER LAB NETWORK INFORMATION =====\n\n"
    f"Hostname: {hostname}\n"
    f"Local IP: {ip}\n"
)

print(result)

with open("data/network_info.txt", "w") as file:
    file.write(result)

print("Saved to: data/network_info.txt")
