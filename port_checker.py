import socket

print("\n===== LOCAL PORT CHECKER =====")

host = "127.0.0.1"
port = int(input("Enter a port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

result = sock.connect_ex((host, port))

if result == 0:
    print("Port", port, "is OPEN")
else:
    print("Port", port, "is CLOSED")

sock.close()
