from scapy.all import *
import random


dest = "35.193.17.254"

load_layer("http")
req = HTTP()/HTTPRequest(
    Accept_Encoding=b'gzip, deflate',
    Cache_Control=b'no-cache',
    Connection=b'keep-alive',
    Host=b'www.secdev.org',
    Pragma=b'no-cache'
)
a = TCP_client.tcplink(HTTP,"35.193.17.254", 8080)
answser = a.sr1(req)
a.close()
print(answser.encode("utf-8"))
