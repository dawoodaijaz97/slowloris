import multiprocessing
import ipaddress

import random
from scapy.all import *

no_of_process = 1
list_process = []
host = "144.217.100.106"
port = 80


def attack():
    block1 = ''
    block2 = ''
    block3 = ''
    block4 = ''
    while True:
        block1 = str(random.randint(10, 127))
        block2 = str(random.randint(10, 255))
        block3 = str(random.randint(10, 255))
        block4 = str(random.randint(10, 255))
        if block1 != "10" and block1 != "172" and block1 != "192":
            break

    ip = block1 + "." + block2 + "." + block3 + "." + block4 + "\\8"
    print(f"Network:{ip}")

    ip_network = ipaddress.ip_network(ip)

    for ip in ip_network:
        print(ip.__str__())


for i in range(0, no_of_process):
    process = multiprocessing.Process(target=attack, )
    process.start()
    list_process.append(process)

for i in range(0, no_of_process):
    list_process[i].join()
