__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append(r'D:\Git\Python')
# 网络设备登录步骤模块
from cisco import Alpha_7_login
# 输入命令返回命令输出模块，返回的是由每一行命令输出组成的列表。
from cisco import Alpha_7_get_command_output



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
command_input = 'ping 192.168.10.1'




a = Alpha_7_login.Login()
c = Alpha_7_get_command_output.Command()
c.set_tn(a.get_tn())
c.set_command_input(command_input)
a.log_in()
d = c.command_get_output()
for line in d:
    print(line)
a.log_out()

