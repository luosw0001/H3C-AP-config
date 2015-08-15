__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telnetlib
import re
import time
import sys
from network_node_tools import get_command_output_1_0


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
tn = telnetlib.Telnet(host, port, timeout=50000)





class Show_info(object):
    def __init__(self, tn=tn):
        self.__tn = tn

    def set_tn(self, tn):
        self.__tn = tn

    def get_tn(self):
        return self.__tn

    def display_dhcp_server_ip_in_use_pool_wlan_ap(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        case.set_command_input('display dhcp server ip-in-use pool wlan_ap ')
        #case.set_command_input('display interface brief')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            if re.match(r'^\s\d*\.\d*\.\d*\.\d*\s*.*', item):
                print(item)
        print(end='\n\n\n')

    def display_wlan_ap_all(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        case.set_command_input('display wlan ap all ')
        #case.set_command_input('display interface brief')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            if re.match(r'^\s.*\s*./.\s*.*\s*.*', item):
                print(item)
        print(end='\n\n\n')

    def display_wlan_ap_connection_record_all(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        case.set_command_input('display wlan ap connection record all ')
        #case.set_command_input('display interface brief')
        case = case.command_get_output()
        #print(case)
        print(end='\n\n\n')
        for item in case:
            #print(item)
            if re.match(r'^\s.*-.*-.*\s*.*', item):
                print(item)
        print(end='\n\n\n')

    def get_display_dhcp_server_ip_in_use_pool_wlan_ap(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        case.set_command_input('display dhcp server ip-in-use pool wlan_ap')
        case = case.command_get_output()
        #print(case)
        display_dhcp_server_ip_in_use_pool_wlan_ap_list = []
        for item in case:
            if re.match(r'^\s\d*\.\d*\.\d*\.\d*\s*.*', item):
                #print(item)
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                display_dhcp_server_ip_in_use_pool_wlan_ap_list.append(item)
        return display_dhcp_server_ip_in_use_pool_wlan_ap_list

    def get_display_wlan_ap_all(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        case.set_command_input('display wlan ap all')
        case = case.command_get_output()
        display_wlan_ap_all_list = []
        for item in case:
            if re.match(r'^\s.*\s*./.\s*.*\s*.*', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                display_wlan_ap_all_list.append(item)
        return display_wlan_ap_all_list

    def get_display_wlan_ap_connection_record_all(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        case.set_command_input('display wlan ap connection record all')
        case = case.command_get_output()
        display_wlan_ap_connection_record_all_list = []
        for item in case:
            if re.match(r'^\s.*-.*-.*\s*.*', item):
                item = re.split('\s*', item)
                for items in item:
                    if items == '':
                        item.remove(items)
                display_wlan_ap_connection_record_all_list.append(item)
        return display_wlan_ap_connection_record_all_list