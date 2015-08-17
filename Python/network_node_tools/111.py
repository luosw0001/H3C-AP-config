__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(*parms):
	print('参数长度是：', len(parms))
	print('第二个参数是：', parms[1])

test(1, '小甲鱼', 3.14, 5, 6, 7, 8)


import re

b = b'\x1b[16D                \x1b[16D Description: AP\r\n Loopback is not set\r\n Media type is twisted pair, Port hardware type is 100_BASE_T\r\n 100Mbps-speed mode, full-duplex mode\r\n Link speed type is autonegotiation, link duplex type is autonegotiation\r\n Flow-control is not enabled\r\n The Maximum Frame Length is 9600\r\n Broadcast MAX-ratio: 100%\r\n Unicast MAX-ratio: 100%\r\n Multicast MAX-ratio: 100%\r\n PVID: 100\r\n Mdi type: auto\r\n Port link-type: access\r\n  Tagged   VLAN ID : none\r\n  Untagged VLAN ID : 100\r\n Port priority: 0\r\n Last clearing of counters:  Never\r\n Peak value of input: 54975 bytes/sec, at 2000-05-06 16:27:54\r\n Peak value of output: 1317963 bytes/sec, at 2000-05-06 16:27:49\r\n Last 300 seconds input:  0 packets/sec 108 bytes/sec 0%\r\n Last 300 seconds output:  1 packets/sec 81 bytes/sec 0%\r\n Input (total):  1951330 packets, 305546141 bytes\r\n\t 1921183 unicasts, 8 broadcasts, 30139 multicasts, 0 pauses\r\n  ---- More ----'

a = r'.*16D\s*.*16D'

d = r'^\s*Description.*'


def format():
	print(b.decode('utf-8'), end='\n\n\n')
	c = re.sub(a, '', b.decode('utf-8'))
	c
	print(c)
	print(re.match(d, c))


format()