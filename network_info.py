import socket

print("\n===== NETWORK INFORMATION =====")

hostname = socket.gethostname()

try:
    ip = socket.gethostbyname(hostname)
except socket.error:
    ip = "Unavailable"

print("Hostname:", hostname)
print("Local IP:", ip)
