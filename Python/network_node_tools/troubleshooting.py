__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telnetlib
import re
import time
import sys
from network_node_tools import interface_info
from network_node_tools import ac_info

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

class Troubleshooting(object):
    def __init__(self, tn=tn):
        self.__tn = tn

    def set_tn(self, tn):
        self.__tn = tn

    def get_tn(self):
        return self.__tn

    def h3c_ip_conflict_detect(self):
        # 根据接入交换机的端口端口类型，mac地址数量判断是否可能地址冲突，但只适用客户端接入同一接入交换机的场景，对于跨交换机IP地址冲突，客户端接入到汇聚及核心交换机场景不适用。




