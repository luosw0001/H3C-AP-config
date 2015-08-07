__author__ = 'TIW'

import sys

sys.path.append(r'D:\Git\Python')

from H3C import wlan_ap_all

from H3C import wlan_ap_connection_record_all


#需求 要显示调用文件的路径及文件名
#print(wlan_ap_all.get_route())


ac_ap_all_list = wlan_ap_all.ac_ap_all()

ac_ap_connection_record_all_list = wlan_ap_connection_record_all.ac_ap_connection_record_all()

target_list = []

for item1 in ac_ap_connection_record_all_list:
    for item2 in ac_ap_all_list:
        if item1[1] == item2[3]:
            target_list.append([item1[1], item2[0], item2[2]])
            #item1[1] SNID, item2[0] AP NAME, item2[2] modle

record1 = []

for item1 in ac_ap_connection_record_all_list:
    record1.append(item1[1])

record2 = []

for item3 in target_list:
    record2.append(item3[0])

final_record = []

for item1 in record1:
    if item1 not in record2:
        final_record.append(item1)

for item in final_record:
    print('There is not OK:', item)
    print()
    print()
    print()



n = 0

for item in target_list:
    print('wlan ap ' + str(item[1]) + ' model ' + item[2])
    print('serial-id ' + item[0])
    print('radio 1')
    print('undo service-template 2')
    if item[1] in ['1f', '2f']:
        print('service-template 1 vlan-id 3000')
    else:
        if int(item[1][:-2]) < 10:
            print('service-template 2 vlan-id 300' + str(item[1][:-2]))
        else:
            print('service-template 2 vlan-id 30' + str(item[1][:-2]))
    print('radio enable')
    print()
    n = n + 1

print('Ap number is:', n)






