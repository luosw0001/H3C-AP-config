__author__ = 'TIW'

import re

filename_core_arp = r'C:\Users\TIW\Desktop\core_arp.txt'

file = open(filename_core_arp, 'r')

caor_arp_list = []

for line in file:
    item = re.split(r'\s*', line)
    while '' in item:
         item.remove('')
    if item[0] == 'Protocol':
        pass
    else:
         caor_arp_list.append(item)

file.close()

def core_arp():
    return caor_arp_list









