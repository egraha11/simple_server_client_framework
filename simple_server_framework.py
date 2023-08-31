import socket

s = socket.socket()

port = 12345

s.bind(("", port))

s.listen()

while True:

    c, address = s.accept()

    print(f"Connection from {address} established")
    
    c.send("Connection made to local host".encode())

    c.close()

    break