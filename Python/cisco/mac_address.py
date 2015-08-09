__author__ = 'TIW'
# -*- coding: utf-8 -*-
import re

#filename_mac_address = 'mac-address.txt'

#filename_mac_address_route = 'C:\Users\TIW\Desktop'

interface_out = ['Gi1/0/25', 'Gi1/0/50', 'CPU']

filename_mac_address = r'C:\Users\TIW\Desktop\mac_address.txt'#.format(filename_mac_address, filename_mac_address_route)

file = open(filename_mac_address, 'r')

mac_address_list = []

for line in file:
    item = re.split(r'\s*', line)
    while '' in item:
         item.remove('')
    if item[3] in interface_out:
         del item
    else:
         mac_address_list.append(item)

for item in mac_address_list:
    print(item)


print('#########################################################################')

file.close()


check_port_list = []

for line in mac_address_list:
    check_port_list.append(int(line[3][6:]))



default_port_list = [x for x in range(1, 25)]

for item in default_port_list:
    if item not in check_port_list:
        mac_address_list.append(['X', 'No--Device--NO', 'No-Device', 'Gi1/0/' + str(item)])


mac_address_list = sorted(mac_address_list, key=lambda item: int(item[3][6:]))


def mac_address():
    return mac_address_list


for item in mac_address_list:
    print(item)



