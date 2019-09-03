from scapy.all import *
from random import randint

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"
ip = "35.193.17.254"
dport = 8080

request = "GET / HTTP/1.1\r\nHost: " + y + "\r\nUser-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1\r\n\r\n"
p = IP(dst=ip) / TCP() / request
out = sr1(p)
if out:
    out.show()
