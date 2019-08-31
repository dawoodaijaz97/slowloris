from scapy.all import *

p = (IP(dst="144.217.100.106") / TCP(dport=80, flags="S"))
syn_ack = sr1(p)
print(type(syn_ack))

