from scapy.all import *
import random

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"

syn = IP(dst='www.google.com') / TCP(dport=80, flags='S')

print(syn.__repr__())

syn_ack = sr1(syn)

print(syn_ack.__repr__())

getStr = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
request = IP(dst='www.google.com') / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr

reply = sr1(request)

print(reply.__repr__())