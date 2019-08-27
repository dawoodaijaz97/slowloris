import socket
import time
import multiprocessing
import os


no_of_process = 3
list_process = []
host = "35.193.17.254"
port = 8080


def create_connection(min_port):
    connections = []
    data = "google"
    for i in range(min_port, min_port + 100):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            pid = os.getpid()
            print(f"Connecting from Process{pid} Port{i}")
            my_socket.bind(("", i))
            my_socket.connect((host, port))
            my_socket.send(data.encode())
            connections.append(my_socket)

        except socket.error:
            print(f"Socket Error")
            my_socket.close()


    def send_data():
        for x in connections:
            try:
                x.send(data.encode())
            except socket.error as msg:
                print(f"Error Sending{msg}")
        time.sleep(10)
        send_data()

    send_data()


for i in range(0, no_of_process):
    starting_port = (i + 3) * 1000
    process = multiprocessing.Process(target=create_connection, args=(starting_port,))
    process.start()
    list_process.append(process)

for i in range(0, no_of_process):
    list_process[i].join()
