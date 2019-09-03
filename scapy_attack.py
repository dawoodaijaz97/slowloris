from scapy.all import *
from random import randint

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"
ip = "35.193.17.254"

sport = int(randint(1025, 65535))
dport = 8080
seq = randint(0,110000)

syn = IP(dst=ip) / TCP(dport=dport, sport=sport, flags='S', seq=seq)
synack = sr1(syn)

print(synack.summary())

seq = synack[TCP].ack
ack = synack[TCP].seq + 1

payload = "GET / HTTP/1.1\r\nHost: " + y + "\r\n\r\n"
request = IP(dst=ip) / TCP(dport=dport, sport=sport, flags='A', seq=seq, ack=ack) / Raw(ensure_bytes(payload))
ans, unans = sr(request)
ans.summary()