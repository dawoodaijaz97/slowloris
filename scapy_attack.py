from scapy.all import *
import random

seq = 12345
dest = "35.193.17.254"
sport = 1040
dport = 80
syn = IP(dst=dest) / TCP(dport=80, flags='S')
max = 20
counter = 0
while counter < max:

    syn = IP(dst=dest) / TCP(sport=random.randint(1025,65500), dport=80, flags='S')

    syn_ack = sr1(syn)
    getStr = 'GET / HTTP/1.1\r\nHost:' + dest + '\r\nAccept-Encoding: gzip, deflate\r\n\r\n'

    out_ack = send(IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))

    sr1(IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='P''A') / getStr)
    counter += 1