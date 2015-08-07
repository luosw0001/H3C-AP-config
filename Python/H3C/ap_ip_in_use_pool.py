__author__ = 'TIW'

import re

filename_ac_dhcp_server_ip_in_use =  'display dhcp server ip-in-use pool wlan_ap.txt'

filename_ac_dhcp_server_ip_in_use_route = 'D:\项目\wk\深圳龙华汽车站店\查找AP\display dhcp server ip-in-use pool wlan_ap'

filename_ac_dhcp_server_ip_in_use = r'{1}\{0}'.format(filename_ac_dhcp_server_ip_in_use, filename_ac_dhcp_server_ip_in_use_route)

file = open(filename_ac_dhcp_server_ip_in_use, 'r')

ac_dhcp_server_ip_in_use_list = []

for line in file:
    item = re.split(r'\s+', line)
    while '' in item:
         item.remove('')
    ac_dhcp_server_ip_in_use_list.append(item)


file.close()

#for item in ac_dhcp_server_ip_in_use_list:
#    print(item)

def ac_dhcp_server_ip_in_use():
    return ac_dhcp_server_ip_in_use_list