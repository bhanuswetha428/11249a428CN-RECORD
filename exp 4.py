import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("HTTP Server running on port", PORT)

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()
    print("Request received:\n", request)

    body = "<html><body><h1>Hello from HTTP Server!</h1></body></html>"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        "Connection: close\r\n\r\n"
        + body
    )

    conn.sendall(response.encode())
    conn.close()

OUTPUT:
HTTP Server running on port 8080
Request received:
 GET / HTTP/1.1
Host: 127.0.0.1
Connection: close


CLIENTS:
import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    "Connection: close\r\n\r\n"
)

client.sendall(request.encode())

response = b""
while True:
    data = client.recv(4096)
    if not data:
        break
    response += data

print("Response from Server:")
print(response.decode())

client.close()

OUTPUT:
Response from Server:
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 57
Connection: close

<html><body><h1>Hello from HTTP Server!</h1></body></html>
