import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

client.sendall(b"Hello server!")
data = client.recv(1024)
print("Server says:", data.decode())

client.close()

""" 


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 This creates a new socket object called client.
 socket.AF_INET: Indicates you're using IPv4.
 socket.SOCK_STREAM: Indicates you're using TCP (reliable, connection-based communication).

---

client.connect(('localhost', 12345))

 This tells the client to connect to the server.
 'localhost': Refers to the local machine (same as 127.0.0.1).
 12345: This must match the port number the server is listening on.
 If the server is not running or the port is wrong, you'll get a ConnectionRefusedError.

---


client.sendall(b"Hello server!")


 Sends a message to the server.
 b"..." makes it a bytes object, which is required for transmission.
 sendall() ensures all data is sent in full.

---


data = client.recv(1024)


 Waits to receive up to 1024 bytes of data from the server.
 This call blocks until some data is received.

---


print("Server says:", data.decode())


 Decodes the received bytes back into a string and prints it.
 decode() uses UTF-8 by default, which matches most text encoding.

---


client.close()


 Closes the connection to the server.
 After this, the client cannot send or receive more data on this socket.


"""