import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen()

print("Server started... Waiting for connection...")
conn, addr = server.accept()
print("Connected by", addr)

data = conn.recv(1024)
print("Received:", data.decode())

conn.sendall(b"Hello from server!")
conn.close()
