__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append(r'D:\Git\Python')
from cisco import Alpha_8_login
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
sysmodtag = ['#', ']']
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
# telnet失败提示
telnet_fail_prompt = [b'Destination unreachable', b'gateway or host down', b'Failed to connect to the remote host']


class Command_without_telnet(object):
    def __init__(self, tn=tn, host=host, username=username, password=password, enable_password=enable_password, enable_command=enable_command, usermodtag=usermodtag, sysmodtag=sysmodtag, login_prompt=login_prompt, password_prompt=password_prompt, command_output_more_tag_prompt=command_output_more_tag_prompt, command_output_more_input_command=command_output_more_input_command, command_input=command_input, telnet_fail_prompt=telnet_fail_prompt):
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
        self.__tn = tn
        self.__telnet_fail_prompt = telnet_fail_prompt

    def set_host(self, host):
        self.__host = host

    def set_port(self, port):
        self.__port = port

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_enable_password(self, enable_password):
        self.__enable_password = enable_password

    def set_enable_command(self, enable_command):
        self.__enable_command = enable_command

    def set_usermodtag(self, usermodtag):
        self.__usermodtag = usermodtag

    def set_sysmodtag(self, sysmodtag):
        self.__sysmodtag = sysmodtag

    def set_login_prompt(self, login_prompt):
        self.__login_prompt = login_prompt

    def set_password_prompt(self, password_prompt):
        self.__password_prompt = password_prompt

    def set_command_output_more_tag_prompt(self, command_output_more_tag_prompt):
        self.__command_output_more_tag_prompt = command_output_more_tag_prompt

    def set_command_output_more_input_command(self, command_output_more_input_command):
        self.__command_output_more_input_command = command_output_more_input_command

    def set_command_input(self, command_input):
        self.__command_input = command_input

    def set_tn(self, tn):
        self.__tn = tn

    def set_command_output_list(self, command_output_list):
        self.__command_output_list = command_output_list

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_enable_password(self):
        return self.__enable_password

    def get_enable_command(self):
        return self.__enable_command

    def get_usermodtag(self):
        return self.__usermodtag

    def get_sysmodtag(self):
        return self.__sysmodtag

    def get_login_prompt(self):
        return self.__login_prompt

    def get_password_prompt(self):
        return self.__password_prompt

    def get_command_output_more_tag_prompt(self):
        return self.__command_output_more_tag_prompt

    def get_command_output_more_input_command(self):
        return self.__command_output_more_input_command

    def get_command_input(self):
        return self.__command_input

    # 传递telnet的进程给get_command_output模块
    def get_tn(self):
        return self.__tn


    def log_in(self):
        # 开启调试，按需开启，方便判断
        # telnetsession.set_debuglevel(2)
        tn = self.__tn
        # 输入CTRL+Z前退出到原始状态
        tn.write(b'\32\n')
        tn.write(b'\32\n')
        tn.write(b'\32\n')
        try:
            # 提示要telnet的网络设备
            print('Telnet的网络设备IP:', self.__host)
            # 输入Telnet命令Telnet网络设备
            tn.write(('telnet ' + self.__host + '\n').encode('utf-8'))
            #time.sleep(0.5)
            #print(tn.read_very_eager())
            # 区配字符，当出现'Username'时，输入用户名
            tn.read_until(self.__login_prompt, 2)
            # 提示登录的用户名
            print('Login Username:', self.__username)
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
            #print('Login successfull', end='\n\n\n\n\n\n')
            try:
                # 暴力进入sysmode，思科华为的命令都输进去，无论什么设备百分百进入。
                # 尝试登录sysmod，输入登录命令
                tn.write(('system-view' + "\n").encode('utf-8'))
                # 提示进入sysmod,以及输入的命令
                #print('Get in sysmod, input command:', self.__enable_command)
                # 输入enable命令
                tn.write((self.__enable_command + "\n").encode('utf-8'))
                # 提升权限时，区配字符，当出现'Password'时，输入密码
                tn.read_until(self.__password_prompt, timeout=1)
                # 提示进入sysmod输入的密码
                #print('Input enable password:', self.__enable_password)
                # 输入enable密码
                tn.write((self.__enable_password + '\n').encode('utf-8'))
                # 提示登录成功
                #print('Login successfull', end='\n\n\n\n\n\n')
                # 一次不行 来两次
                tn.write(self.__command_output_more_input_command.encode('utf-8'))
                tn.write(self.__command_output_more_input_command.encode('utf-8'))
                tn.write(self.__command_output_more_input_command.encode('utf-8'))
                # 暴力进入sysmode，思科华为的命令都输进去，无论什么设备百分百进入。
                # 尝试登录sysmod，输入登录命令
                tn.write(('system-view' + "\n").encode('utf-8'))
                # 提示进入sysmod,以及输入的命令
                #print('Get in sysmod, input command:', self.__enable_command)
                # 输入enable命令
                tn.write((self.__enable_command + "\n").encode('utf-8'))
                # 提升权限时，区配字符，当出现'Password'时，输入密码
                tn.read_until(self.__password_prompt, timeout=1)
                # 提示进入sysmod输入的密码
                #print('Input enable password:', self.__enable_password)
                # 输入enable密码
                tn.write((self.__enable_password + '\n').encode('utf-8'))
                # 提示登录成功
                #print('Login successfull', end='\n\n\n\n\n\n')
            except:
                pass
            tn.write(self.__command_output_more_input_command.encode('utf-8'))
            tn.write(self.__command_output_more_input_command.encode('utf-8'))
            tn.write(self.__command_output_more_input_command.encode('utf-8'))
        except:
            print('Telnet网络设备:', self.__host, '未响应')

    # 结束Telnet进程
    def log_out(self):
        self.__tn.close()
        print('Logout!!!')
