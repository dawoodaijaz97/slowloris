import socket
no_of_process = 3
list_process = []
host = "35.193.17.254"
port = 8080
data = "google"
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    my_socket.connect((host, port))
    my_socket.send(data.encode())
    data = my_socket.recv(1024)
    print(data)
except socket.error:
    print(f"Socket Error")
    my_socket.close()
