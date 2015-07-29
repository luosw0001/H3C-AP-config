__author__ = 'TIW'

import re

filename_ac_ap_connection_record_all =  'display wlan ap connection record all.txt'

filename_ac_ap_connection_record_all = r'D:\项目\wk\维尔纳工程标准\预配\查找AP\display wlan ap connection record all\{0}'.format(filename_ac_ap_connection_record_all)

file = open(filename_ac_ap_connection_record_all, 'r')

ac_ap_connection_record_all_list = []

for line in file:
    item = re.split(r'\s+', line)
    while '' in item:
         item.remove('')
    ac_ap_connection_record_all_list.append(item)


file.close()

#for item in ac_ap_connection_record_all_list:
#    print(item)


def ac_ap_connection_record_all():
    return ac_ap_connection_record_all_list