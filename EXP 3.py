import socket

hostname = socket.gethostname()
ip_addresses = socket.getaddrinfo(hostname, None)

print("IP Addresses of the System:")

for address in ip_addresses:
    ip = address[4][0]
    print(ip)

OUTPUT:
IP Addresses of the System:
127.0.0.1
192.168.1.5
