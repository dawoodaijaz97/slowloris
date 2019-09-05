from scapy.all import *
from random import randint

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"
ip = "35.193.17.254"
dport = 8080


i = IP()
i.dst = ip
print ("IP layer prepared: ", i.summary())

t = TCP()
t.dport = dport
t.sport = sp
t.flags = "S"
print("Sending TCP SYN Packet: ", t.summary())
ans = sr1(i/t)
print("Reply was: ",ans.summary())

t.seq = ans.ack
t.ack = ans.seq + 1
t.flags = "A"
print("Sending TCP ACK Packet: ", t.summary())
ans = sr(i/t/"X")