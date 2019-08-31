from scapy.all import *
import random

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"

request = "GET / HTTP/1.1\r\nHost: " + y + "\r\n\r\n"
p = IP(dst=x) / TCP() / request
out = sr1(p)
if out:
    out.show()
