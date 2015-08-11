__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telnetlib
import re
import time
import sys

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
command_input = 'show mac dynamic'



class Login(object):
    def __init__(self, host=host, port=port, username=username, password=password, enable_password=enable_password, enable_command=enable_command, usermodtag=usermodtag, sysmodtag=sysmodtag, login_prompt=login_prompt, password_prompt=password_prompt, command_output_more_tag_prompt=command_output_more_tag_prompt, command_output_more_input_command=command_output_more_input_command, command_input=command_input):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__enable_password = enable_password
        self.__enable_command = enable_command
        self.__usermodtag = usermodtag
        self.__sysmodtag = sysmodtag
        self.__login_prompt = login_prompt
        self.__password_prompt = password_prompt
        self.__command_output_more_tag_prompt = command_output_more_tag_prompt
        self.__command_output_more_input_command = command_output_more_input_command
        self.__command_input = command_input
        self.__tn = telnetlib.Telnet(self.__host, self.__port, timeout=50000)

    # 传递telnet的进程给get_command_output模块
    def get_tn(self):
        return self.__tn

    def log_in(self):
        # 实例化telnet对象，建立一个主机连接
        tn = self.__tn
        # 开启调试，按需开启，方便判断
        # telnetsession.set_debuglevel(2)
        # 区配字符，当出现'Username'时，输入用户名
        tn.read_until(self.__login_prompt)
        # 提示输入的用户名
        print('Input Username:', self.__username)
        # 输入用户名
        tn.write((self.__username + '\n').encode('utf-8'))
        # 区配字符，当出现'Password'时，输入密码
        tn.read_until(self.__password_prompt)
        # 提示输入的密码
        print('Input Password:', self.__password)
        # 输入密码
        tn.write((self.__password + '\n').encode('utf-8'))
        # 如果登录Usermode成功，则出现类似>,使用UsermodTag来进行捕获
        tn.read_until(self.__usermodtag)
        print('Get in sysmod, input command:', self.__enable_command)
        tn.write((self.__enable_command + "\n").encode('utf-8'))
        # 提升权限时，区配字符，当出现'Password'时，输入密码
        tn.read_until(self.__password_prompt)
        # 提示进入sysmod输入的密码
        print('Input enable password:', self.__enable_password)
        # 输入enable密码
        tn.write((self.__enable_password + '\n').encode('utf-8'))
        print('Login OK!!!')

    # 结束Telnet进程
    def log_out(self):
        self.__tn.close()
        print('Logout!!!')



            
           
           
           

