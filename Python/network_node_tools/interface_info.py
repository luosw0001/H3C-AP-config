__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telnetlib
import re
import time
import sys
from network_node_tools import get_command_output_1_0
from network_node_tools import get_command_output_1_1

### 网络设备IP
host = '218.17.209.74'
### 网络设备telnet端口
port = 60001
### 登录帐号
username = 'admin'
### 登录密码
password = 'admin@123'
### enable密码
enable_password = 'admin@123'
### enable命令
enable_command = 'en'
### Usermode提示符
usermodtag = b'>'
### Sysmode提示符
sysmodtag = [b'#', b']']
### 登录网络设备时提示输入账号的提示
login_prompt = b'Username'
### 登录网络设备时提示输入密码的提示
password_prompt = b'Password'
### 输入命令返回值未完结提示符
command_output_more_tag_prompt = b'More'
### 输入命令返回值未完结时输入的命令
command_output_more_input_command = '\n'
### 输入的命令
command_input = 'show mac dynamic'
### 默认telnet
#tn = telnetlib.Telnet(host, port, timeout=50000)
tn = telnetlib.Telnet()


# 思路说明：查看命令的function都是先获取命令的输出，但这个输出是含非必要信息，然后利用正则表达式把需要的信息提取出来，对于返回命令输出的function是在查看命令function的基础上删除''然后返回命令输出组成的列表


class Show_int(object):
    def __init__(self, tn=tn):
        self.__tn = tn
        #self.__case = get_command_output_1_0.Command()
        self.__case = get_command_output_1_1.Command()

    def set_tn(self, tn):
        self.__tn = tn

    def get_tn(self):
        return self.__tn

    def show_interface_status(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('show interface status ')
        #case.set_command_input('display interface brief')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            if re.match(r'^Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet', item):
                print(item)
        print(end='\n\n\n')

    def show_ip_arp(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('show ip arp ')
        #case.set_command_input('display interface brief')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            if re.match(r'^Internet', item):
                print(item)
        print(end='\n\n\n')

    def display_int_brief(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        #case.set_command_input('show interface status ')
        case.set_command_input('display interface brief')
        case = case.command_get_output()
        # print('DDDDDDDDDDDDDDDD', case, 'DDDDDDDDDDDDDDDDDDDDDD')
        print(end='\n\n\n')
        for item in case:
            #print(item)
            if re.match(r'^Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet', item):
                print(item)
        print(end='\n\n\n')

    def display_poe_interface(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('display poe interface ')
        #case.set_command_input('display interface brief')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            if re.match(r'\s*(Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet)\s*', item):
                print(item)
        print(end='\n\n\n')

    def show_mac_address_table(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        #case.set_command_input('show interface status ')
        case.set_command_input('show mac-address-table')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            #print(item)
            if re.match(r'.*Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet.*', item):
                print(item)
        print(end='\n\n\n')

    def display_mac_address(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        #case.set_command_input('show interface status ')
        case.set_command_input('display mac-address')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            #print(item)
            if re.match(r'.*Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet.*', item):
                print(item)
        print(end='\n\n\n')

    def display_interface(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        #case.set_command_input('show interface status ')
        case.set_command_input('display interface')
        case = case.command_get_output()
        #print(case)
        print(end='\n\n\n')
        for item in case:
            print(item)
            #if re.match(r'.*Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet.*', item):
            #    print(item)
        print(end='\n\n\n')

    def get_display_mac_address(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('display mac-address')
        case = case.command_get_output()
        display_mac_address_list = []
        for item in case:
            if re.match(r'.*Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet.*', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                display_mac_address_list.append(item)
        return display_mac_address_list

    def get_show_interface_status(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('show interface status')
        case = case.command_get_output()
        #print(case)
        show_interface_status_list = []
        for item in case:
            if re.match(r'^Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                show_interface_status_list.append(item)
        return show_interface_status_list

    def get_show_ip_arp(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('show ip arp')
        case = case.command_get_output()
        show_ip_arp_list = []
        for item in case:
            if re.match(r'^Internet', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                show_ip_arp_list.append(item)
        return show_ip_arp_list

    def get_display_int_brief(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('display interface brief')
        case = case.command_get_output()
        display_int_brief_list = []
        for item in case:
            if re.match(r'^Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                display_int_brief_list.append(item)
        return display_int_brief_list

    def get_display_poe_interface(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('display poe interface')
        case = case.command_get_output()
        display_poe_interface_list = []
        for item in case:
            if re.match(r'\s*(Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet)\s*', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                display_poe_interface_list.append(item)
        return display_poe_interface_list

    def get_show_mac_address_table(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        case.set_command_input('show mac-address-table')
        case = case.command_get_output()
        show_mac_address_table_list = []
        for item in case:
            if re.match(r'.*Ethernet|Eth|GE|GI|FastEthernet|GigabitEthernet.*', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                show_mac_address_table_list.append(item)
        return show_mac_address_table_list

    def get_display_interface(self):
        tn = self.__tn
        # 实例化
        case = self.__case
        case.set_tn(tn)
        #case.set_command_input('show interface status ')
        case.set_command_input('display interface')
        case = case.command_get_output()
        print(end='\n\n\n')
        # 提取所需的借口名字、接口描述、接口状态、接口类型信息，其余删除
        list_one = []
        for item in case:
            #print(item)
            if re.match(r'^\sEthernet\d*/*\d*/*\d*\s.*|\sEth\d*/*\d*/*\d*\s.*|\sGE\d*/*\d*/*\d*\s.*|\sGI\d*/*\d*/*\d*\s.*|\sFastEthernet\d*/*\d*/*\d*\s.*|\sGigabitEthernet\d*/*\d*/*\d*\s.*|^\s*Description.*|^\s*Port link-type.*', item):
                list_one.append(item)
        # print(list_one)
        # 将提取的信息进一步精简，格式化为列表，好提供上层处理。
        list_two = []
        n = 0
        while n < (len(list_one) - 2):
            list_two.append([list_one[n], list_one[n + 1], list_one[n + 2]])
            n = n + 3
        # print(list_two)
        display_interface_list = []
        for item in list_two:
            # a = 接口名字, b = 接口描述
            # print(item[0])
            a, b = re.split(' current state: ', item[0])
            # 接口描述
            # b = re.split(' current state: ', item[0])[1]
            # 接口状态
            c = re.split(': ', item[1])[1]
            # 接口类型
            d = re.split(': ', item[2])[1]
            # 输出的列表格式为[接口名字, 接口描述, 接口状态, 接口类型]
            display_interface_list.append([a, b, c, d])
        for item in display_interface_list:
            print(item)
        print(end='\n\n\n')



