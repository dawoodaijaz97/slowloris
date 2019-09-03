from scapy.all import *
from random import randint

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"
ip = "35.193.17.254"
dport = 8080

request = "GET / HTTP/1.1\r\nHost: " + y + "\r\n\r\n"
p = IP(dst=ip) / TCP() / request
out = sr1(p)
if out:
    out.show()
