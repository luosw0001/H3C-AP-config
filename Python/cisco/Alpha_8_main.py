__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append(r'D:\Git\Python')
# 网络设备登录步骤模块
from cisco import Alpha_8_login
# 输入命令返回命令输出模块，返回的是由每一行命令输出组成的列表。
from cisco import Alpha_8_get_command_output
from cisco import Alpha_8_login_without_telnet



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





a = Alpha_8_login.Login()
a.log_in()
tn = a.get_tn()
i = Alpha_8_get_command_output.Command()
i.set_tn(tn)
i.set_command_input('show run')
i = i.command_get_output()
for line in i:
    print(line)
a.log_out()


#  实例化telnet对象
a = Alpha_8_login.Login()
#a.set_host(host)
#a.set_port(port)
# 建立一个主机连接,登录核心交换机
a.log_in()
# 获取Telnet进程
tn = a.get_tn()
# 输入命令Telnet接入交换机
#b = Alpha_8_get_command_output.Command()
#b.set_tn(tn)
#b.set_command_input(command_input)
#c = b.command_get_output()
#for line in c:
#    print(line)
d = Alpha_8_login_without_telnet.Command_without_telnet()
d.set_tn(tn)
d.set_host('192.168.10.208')
d.log_in()
e = Alpha_8_login_without_telnet.Command_without_telnet()
e.set_tn(tn)
e.set_host('192.168.10.253')
e.log_in()
f = Alpha_8_login_without_telnet.Command_without_telnet()
f.set_tn(tn)
f.set_host('192.168.10.208')
f.log_in()
h = Alpha_8_get_command_output.Command()
h.set_tn(tn)
h.set_command_input('display interface brief ')
k = h.command_get_output()
for line in k:
    print(line)
h.set_command_input('display current-configuration')
k = h.command_get_output()
for line in k:
    print(line)
a.log_out()