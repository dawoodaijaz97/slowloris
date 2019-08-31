from scapy.all import *
import random

dest = "35.193.17.254"
user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"

syn = IP(dst=dest) / TCP(dport=80, flags='S')

syn_ack = sr1(syn)

out_ack = send(
    IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))
getStr = f'GET / HTTP/1.1\r\nHost:{dest}\r\nAccept-Encoding: gzip, deflate\r\nUser-agent:{user_agent}\r\n\r\n'
reply = sr1(IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1,
                               flags=['P', 'A']) / getStr)

print(reply.__repr__())
