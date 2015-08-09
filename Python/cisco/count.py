__author__ = 'TIW'

import sys

sys.path.append(r'D:\Git\Python')

from cisco import mac_address

from cisco import core_arp

core_arp = core_arp.core_arp()

mac_address = mac_address.mac_address()0

mac_to_ip = []

for item1 in mac_address:
    for item2 in core_arp:
        if item1[1] == item2[3]:
            mac_to_ip.append([item1[1], item2[1], item1[3]])



for item in mac_to_ip:
    print(item)


import xlsxwriter

workbook = xlsxwriter.Workbook('camera.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(1, 1, 'serial id')
worksheet.write(1, 2, 'AP name')
worksheet.write(1, 3, 'model')
worksheet.write(1, 4, 'mac adddress')
worksheet.write(1, 5, 'AP IP adddress')
worksheet.write(1, 6, 'port')
worksheet.write(1, 7, 'Switch')
worksheet.write(1, 8, 'Switch IP adddress')

row = 2
col = 1

for item in target_list:
    worksheet.write(row, col, item[0])
    worksheet.write(row, col + 1, item[1])
    worksheet.write(row, col + 2, item[2])
    worksheet.write(row, col + 3, item[3])
    worksheet.write(row, col + 4, item[4])
    worksheet.write(row, col + 5, item[5])
    row += 1

workbook.close()