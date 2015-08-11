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


class Command(object):
    def __init__(self, tn, host=host, port=port, username=username, password=password, enable_password=enable_password, enable_command=enable_command, usermodtag=usermodtag, sysmodtag=sysmodtag, login_prompt=login_prompt, password_prompt=password_prompt, command_output_more_tag_prompt=command_output_more_tag_prompt, command_output_more_input_command=command_output_more_input_command, command_input=command_input):
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
        self.__command_output_list = []

    def command_get_output(self):
        tn = self.__tn
        # 输入命令以获取网络设备的hostname
        tn.write(('\n').encode('utf-8'))
        # 命令返回值前两个输出不是期望的返回值而是空值,用此命令获取下一个返回值
        hostname = tn.read_some()
        # 命令返回值前两个输出不是期望的返回值而是空值,用此命令获取下一个返回值
        hostname = tn.read_some()
        # 获取网络设备的hostname
        hostname = (tn.read_some()).decode('utf-8')
        tn.write(('\n').encode('utf-8'))
        # 如果登录Sysmode成功，则出现类似#,使用SysmodTag来进行捕获
        tn.read_until(self.__sysmodtag)
        # 提示输入的命令
        print('Input command:', self.__command_input)
        # 输入命令
        tn.write((self.__command_input + '\n').encode('utf-8'))
        # 将输入命令的返回值赋值response,命令返回值前两个输出不是期望的返回值而是空值
        response = tn.read_very_eager()
        print(response)
        # 将输入命令的返回值赋值response，如果sysmodtag在response则表示命令输出完整，否则输入命令获取完整的命令
        if self.__sysmodtag not in response:

            n = 1
            while self.__sysmodtag not in response:
                for i in range(2):### range(2)里面这个2是有讲究的不能少于1最好是2
                    # 命令返回值未完结时，输入继续输出命令获取值的命令
                    tn.write(self.__command_output_more_input_command.encode('utf-8'))
                    # 获取命令返回值并赋值给response， 用response捕获命令结束提示
                    response = tn.read_until(self.__command_output_more_tag_prompt, timeout=0.5)
                    # 将获取命令返回值赋值给response_format
                    response_format = response
                    # 将response_format重新编码
                    response_format = response_format.decode('utf-8')
                    # 将response_format格式化
                    response_format = re.sub(r'\x08', '', response_format)
                    response_format = re.sub(r'--           ', '', response_format)
                    response_format = re.split(r'\r\n', response_format)
                    # 删除命令的返回值中对于的无效返回值
                    for item in response_format:
                        if self.__command_output_more_tag_prompt.decode('utf-8') in item:
                            response_format.remove(item)
                    # 将输入命令的返回值添加到列表
                    for item in response_format:
                        self.__command_output_list.append(item)
                    # 提示正在获取命令返回值
                    #print(response)
                    print('Getting command output, please wait.',  n, 'lines command output had gotten.')
                    n = n + 1
            # 获取完整的命令输出后提示完成
            print('All command output had gotten!!!')
        #### 这些代码没用了，但是先留着可能有用    ###
        #else:
        #    print(2229)
        #    response_format = response
        #print(response_format)
        #    response_format = response_format.decode('utf-8')
        #    response_format = re.split(r'\r\n', response_format)
        #    for item in response_format:
        #        print(item)
        #### 这些代码没用了，但是先留着可能有用    ###

        for item in self.__command_output_list:
            if hostname in item:
                self.__command_output_list.remove(item)
        for item in self.__command_output_list:
            if self.__command_output_more_tag_prompt.decode('utf-8') in item:
                self.__command_output_list.remove(item)
        return self.__command_output_list




