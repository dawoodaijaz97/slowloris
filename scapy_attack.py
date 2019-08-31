from scapy.all import *
import random

x = "35.193.17.254"
y =x
request = "GET / HTTP/1.1\r\nHost: " + y + "\r\n"
p = IP(dst=x) / TCP() / request
out = sr1(p)
if out:
    out.show()