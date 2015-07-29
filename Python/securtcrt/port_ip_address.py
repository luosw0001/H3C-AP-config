__author__ = 'TIW'
#桌面上建立两个文件，core_arp.txt用来存储核心交换机的ARP表，mac_address.txt用来存储接入交换机的mac地址表


#import xlsxwriter
import re
import xlrd
import xlwt



#----------------处理核心交换机的ARP表--------------------------
filename_core_arp =  'core_arp.txt'
#核心交换机arp表
filename_core_arp = r'C:\Users\TIW\Desktop\{0}'.format(filename_core_arp)
f = open(filename_core_arp, 'r')

d = []
#空的列表

for line in f:
    c = re.split(r'\s*', line)
    #将文本行内容提取清洗并放入列表c
    while '' in c:
        c.remove('')
    biaoti = ['Protocol', 'Address', 'Age', '(min)', 'Hardware', 'Addr', 'Type', 'Interface']
    #删除列表内的无用标题
    d.append(c)
    while biaoti in d:
        d.remove(biaoti)


f.close()

#for a in d:
#    print(a)

#----------------处理核心交换机的ARP表--------------------------



#----------------处理接入交换机的mac地址表--------------------------
filename_mac_address =  'mac_address.txt'
#接入交换机mac地址表
interface_out = ['Gi1/0/49', 'Gi1/0/50', 'Gi1/0/51', 'Gi1/0/52']
#交换机上联接口名字
filename_mac_address = r'C:\Users\TIW\Desktop\{0}'.format(filename_mac_address)
mac_address = open(filename_mac_address, 'r')

e = []

for line in mac_address:
    c = re.split(r'\s*', line)
    #将文本行内容提取清洗并放入列表c
    while '' in c:
        c.remove('')
    #删除列表内空的值
    if c[3] in interface_out:
        del c
    #删除来源于交换机上联接口的mac地址
    else:
        e.append(c)



mac_address.close()

#for a in e:
#    print(a)

#----------------处理接入交换机的mac地址表--------------------------



#----------------生成接入交换机端口、ip、mac地址、vlan关系表--------------------------


#如果核心交换机的arp表中的mac地址与接入交换机的mac地址表里面的mac地址对应，则将这个ip、mac地址、接入交换机端口、vlan写入列表f
f = []

for item_in_e in e:
    for item_in_d in d:
        if item_in_d[3] == item_in_e[1]:
            f.append([item_in_d[1], item_in_e[1], int(item_in_e[3][6:]), item_in_e[0]])


#连接接入交换机的设备如果没有IP地址的情况
k = []
for item_in_f in f:
    k.append(int(item_in_f[2]))

for item_in_e in e:
    if item_in_e[2] == 'DYNAMIC':
        if int(item_in_e[3][6:]) not in k:
            f.append(['No_Ip', item_in_e[1], int(item_in_e[3][6:]), item_in_e[0]])


#接入交换机没有连接设备的情况
l = []
for item_in_f in f:
    l.append(int(item_in_f[2]))

for x in range(1, 49):
    if x not in l:
        f.append(['No_Device', 'No_Device', x, 'No_Device'])

f = sorted(f, key=lambda a: a[2])



for a in f:
    print(a)


