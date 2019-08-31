from scapy.all import *

p = (IP(dst="144.217.100.106") / TCP(dport=80, flags="S"))
syn_ack = sr1(p)
print(str(syn_ack.__repr__()))
getStr = 'GET / HTTP/1.1\r\n\r\n'

request = IP(dst="144.217.100.106") / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
reply = sr1(p)
print(reply.__repr__())