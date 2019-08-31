from scapy.all import *
import random

x = "instance2mymachines.xyz"
y = "www.instance2mymachines.xyz"

load_layer("http")
req = HTTP()/HTTPRequest(
    Accept_Encoding=b'gzip, deflate',
    Cache_Control=b'no-cache',
    Connection=b'keep-alive',
    Host=b'www.instance2mymachines.xyz',
    Pragma=b'no-cache'
)
a = TCP_client.tcplink(HTTP,y, 8080)
answser = a.sr1(req)
a.close()
with open("www.instance2mymachines.xyz.html", "wb") as file:
    file.write(answser.load)