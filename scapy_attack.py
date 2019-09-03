from scapy.all import *
import random

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"

syn = IP(dst=y) / TCP(dport=8080, flags='S')

print(syn.__repr__())

syn_ack = sr1(syn)

print(syn_ack.__repr__())

getStr = 'GET / HTTP/1.1\r\nHost: www.instance2mymachines.xyz\r\n\r\n'
request = IP(dst=y) / TCP(dport=8080, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr

reply,unans = sr1(request)

reply.summary()

print(reply.__repr__())