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
        self.__tn = telnetlib.Telnet()

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
        tn = self.__tn
        try:
            # 提示要telnet的网络设备和端口
            print('网络设备IP:', self.__host, '端口:', self.__port)
            # 实例化telnet对象，建立一个主机连接
            tn.open(self.__host, self.__port, timeout=5)
            print('Telnet successfull')
            # 开启调试，按需开启，方便判断
            # telnetsession.set_debuglevel(2)
            # 区配字符，当出现'Username'时，输入用户名
            try:
                tn.read_until(self.__login_prompt, 2)
                # 提示登录的用户名
                print('Login Username:', self.__username)
                # 输入用户名
                tn.write((self.__username + '\n').encode('utf-8'))
            except:
                pass
            # 区配字符，当出现'Password'时，输入密码
            tn.read_until(self.__password_prompt)
            # 提示输入的密码
            print('Input Password:', self.__password)
            # 输入密码
            tn.write((self.__password + '\n').encode('utf-8'))
            # 如果登录Usermode成功，则出现类似>,使用UsermodTag来进行捕获
            tn.read_until(self.__usermodtag)
            print('Get in sysmod, input command:', self.__enable_command)
            # 输入enable命令
            tn.write((self.__enable_command + "\n").encode('utf-8'))
            # 提升权限时，区配字符，当出现'Password'时，输入密码
            tn.read_until(self.__password_prompt)
            # 提示进入sysmod输入的密码
            print('Input enable password:', self.__enable_password)
            # 输入enable密码
            tn.write((self.__enable_password + '\n').encode('utf-8'))
            print('Login successfull', end='\n\n\n\n\n\n')

        except:
            print('网络设备IP:', self.__host, '端口:', self.__port, '未响应')



    # 结束Telnet进程
    def log_out(self):
        self.__tn.close()
        print('Logout!!!')



