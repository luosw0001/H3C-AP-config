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





class Display_int_brief(object):
    def __init__(self, tn=tn):
        self.__tn = tn

    def set_tn(self, tn):
        self.__tn = tn

    def get_tn(self):
        return self.__tn


    def display_int_brief(self):
        tn = self.__tn
        # 实例化
        case = get_command_output_1_0.Command()
        case.set_tn(tn)
        #case.set_command_input('show interface status ')
        case.set_command_input('display interface brief')
        case = case.command_get_output()
        print(end='\n\n\n')
        for item in case:
            if re.match(r'^Eth|GE|GI|FastEthernet|GigabitEthernet', item):

                print(item)
        print(end='\n\n\n')

