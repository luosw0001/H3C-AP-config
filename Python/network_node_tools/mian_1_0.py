__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append(r'D:\Git\Python')
# 网络设备telnet登录模块
from network_node_tools import login_1_0
# 输入命令返回命令输出模块，返回的是由每一行命令输出组成的列表。
from network_node_tools import get_command_output_1_0
# 网络设备非telnet登录模块
from network_node_tools import login_without_telnet_1_0

from network_node_tools import interface_info
from network_node_tools import ac_info

### 网络设备IP
host = '119.145.96.98'
### 网络设备telnet端口
port = 5742
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
sysmodtag = b'#'
### 登录网络设备时提示输入账号的提示
login_prompt = b'Username'
### 登录网络设备时提示输入密码的提示
password_prompt = b'Password'
### 输入命令返回值未完结提示符
command_output_more_tag_prompt = b'More'
### 输入命令返回值未完结时输入的命令
command_output_more_input_command = '\n'
### 输入的命令
command_input = 'show run'








#  实例化telnet对象

def test_all():

    a = login_1_0.Login()
    a.log_in()
    tn = a.get_tn()
    c = interface_info.Show_int()
    c.set_tn(tn)
    c.show_interface_status()
    for item in c.get_show_interface_status():
        print(item)
    c.show_mac_address_table()
    for item in c.get_show_mac_address_table():
        print(item)
    c.show_ip_arp()
    for item in c.get_show_ip_arp():
        print(item)
    f = login_without_telnet_1_0.Command_without_telnet()
    f.set_tn(tn)
    f.set_host('192.168.10.208')
    f.log_in()
    b = interface_info.Show_int()
    b.set_tn(tn)
    b.display_int_brief()
    for item in b.get_display_int_brief():
        print(item)
    b.display_mac_address()
    k = b.get_display_mac_address()
    for item in k:
        print(item)
    b.display_poe_interface()
    for item in b.get_display_poe_interface():
        print(item)
    g = login_without_telnet_1_0.Command_without_telnet()
    g.set_tn(tn)
    g.set_host('192.168.10.100')
    g.log_in()
    h = ac_info.Show_info()
    h.set_tn(tn)
    h.display_dhcp_server_ip_in_use_pool_wlan_ap()
    for item in h.get_display_dhcp_server_ip_in_use_pool_wlan_ap():
        print(item)
    h.display_wlan_ap_all()
    for item in h.get_display_wlan_ap_all():
        print(item)
    h.display_wlan_ap_connection_record_all()
    for item in h.get_display_wlan_ap_connection_record_all():
        print(item)
    a.log_out()

#test_all()


a = login_1_0.Login()
a.log_in()
tn = a.get_tn()
f = login_without_telnet_1_0.Command_without_telnet()
f.set_tn(tn)
f.set_host('192.168.10.208')
f.log_in()
b = interface_info.Show_int()
b.set_tn(tn)
b.get_display_interface()
a.log_out()


































