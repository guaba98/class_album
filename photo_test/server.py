import socket

HOST = "10.10.20.103"
PORT = 1121

s = socket.socket()
s.bind((HOST, PORT))

data = open(r'의기소침_핑구.jpg', 'rb').read()
print("Waiting  for connection...")

s.listen(5)
while True:
    client, client_address = s.accept()
    print(client_address, "is connected")
    client.send(data)
    client.shutdown(socket.SHUT_WR)   # notify that nothing more is to be sent
    _ = client.recv(16)               # wait for the client to close when everything has been received
    client.close()                    # Ok, we can explicitely close