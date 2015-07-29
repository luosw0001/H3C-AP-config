__author__ = 'TIW'



filename_ap =  'arp3.txt'
#目标文件名
filename_xls = 'TestData3.xls'

n = 8
#AP的IP地址开始地址
AP_address_head = '10.0.0.'
AP_address_trailer = ' 255.0.0.0'
#AP的IP地址设置
interface_out = 'Et0/0'
#交换机上联接口名字



#import xlsxwriter
import re
import xlrd
import xlwt






filename_ap = r'C:\Users\TIW\Desktop\{0}'.format(filename_ap)
filename_xls = r'C:\Users\TIW\Desktop\{0}.xls'.format(filename_xls)

f = open(filename_ap, 'r')

e = []
d = []
#空的列表





for line in f:
    c = re.split(r'\s*', line)
    #将文本行内容提取清洗并放入列表c
    while '' in c:
        c.remove('')
    #删除列表内空的值
    if c[3] == interface_out:
        del c
    #删除来源于交换机上联接口的mac地址
    else:
        vlan, mac, typ, interface = c

        #print(d)
        #print(mac)
        print('ip dhcp pool ' + str(mac))
        print('host ' + AP_address_head + str(n) + AP_address_trailer)
        print('client-identifier ' + '01' + mac[0:2] + '.' + mac[2:4] + mac[5:7] + '.' + mac[7:9] + mac[10:12] + '.' + mac[12:14])
        c.append(AP_address_head + str(n) + AP_address_trailer)
        n = n + 1
        d.append(c)
        #print(n)
        print()


f.close()


g = len(d)
print(d)
print(e)
print(g)

wbk = xlwt.Workbook(encoding='utf-8', style_compression = 0)
sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok = True)

sheet.write(0, 0, 'Location')
sheet.write(0, 1, 'AP Name')
sheet.write(0, 2, 'AP Description')
sheet.write(0, 3, 'MAC Address')
sheet.write(0, 4, 'S/N Number')
sheet.write(0, 5, 'Switch IP Address')
sheet.write(0, 6, 'Switch Port')
sheet.write(0, 7, 'Remark')
sheet.write(0, 8, 'AP ip')

for i in range(g):
    print(i)
    sheet.write((i + 1), 3, d[i][1])
    sheet.write((i + 1), 6, d[i][3])
    sheet.write((i + 1), 8, d[i][4])




wbk.save(filename_xls)
