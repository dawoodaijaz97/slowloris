from scapy.all import *


seq = 12345
dest = "35.193.17.254"
sport = 1040
dport = 8080
syn = IP(dst=dest) / TCP(dport=80, flags='S')

# GET SYNACK
syn_ack = sr1(syn)
# Send ACK
out_ack = send(
    IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))

# Send the HTTP GET
getStr = 'GET / HTTP/1.1\r\nHost:' + dest+'\r\n\r\n'
reply = sr1(IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1,flags='P''A') / getStr)
print(reply.__repr__())
