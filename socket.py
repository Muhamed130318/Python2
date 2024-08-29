import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET means it will use ipv4 and SOCK_STREAM means it will use TCP.

s.connect(("192.168.50.101", 9999))

print(s.recv(1024))

s.close()

