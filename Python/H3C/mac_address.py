__author__ = 'TIW'

import re

filename_S2626_mac_address =  'display mac-address.txt'

filename_S2626_mac_address_route = 'D:\项目\wk\深圳龙华汽车站店\查找AP\display mac-address'

interface_out = ['GigabitEthernet1/0/25', 'GigabitEthernet1/0/26']

filename_S2626_mac_address = r'{1}\{0}'.format(filename_S2626_mac_address, filename_S2626_mac_address_route)

file = open(filename_S2626_mac_address, 'r')

S2626_mac_address_list = []

for line in file:
    item = re.split(r'\s*', line)
    while '' in item:
         item.remove('')
    if item[3] in interface_out:
         del item
    else:
         S2626_mac_address_list.append(item)


file.close()

check_port_list = []

for line in S2626_mac_address_list:
    check_port_list.append(int(line[3][12:]))

default_port_list = [x for x in range(1, 25)]

for item in default_port_list:
    if item not in check_port_list:
        S2626_mac_address_list.append(['ffff-ffff-ffff', '0', 'No-Device', 'Ethernet1/0/' + str(item), 'No-Device'])


S2626_mac_address_list = sorted(S2626_mac_address_list, key=lambda item: int(item[3][12:]))

for line in S2626_mac_address_list:
    print(line)

def S2626_mac_address():
    return S2626_mac_address_list

