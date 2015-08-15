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



class Command(object):
    def __init__(self, tn=tn, host=host, port=port, username=username, password=password, enable_password=enable_password, enable_command=enable_command, usermodtag=usermodtag, sysmodtag=sysmodtag, login_prompt=login_prompt, password_prompt=password_prompt, command_output_more_tag_prompt=command_output_more_tag_prompt, command_output_more_input_command=command_output_more_input_command, command_input=command_input):
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

    def get_tn(self):
        return self.__tn

    def get_command_output_list(self):
        return self.__command_output_list


    def command_get_output(self):
        tn = self.__tn
        # 输入CTRL+Z前退出到原始状态
        tn.write(b'\32\n')
        #tn.write(b'\32\n')
        #tn.write(b'\32\n')
        #tn.write(self.__command_output_more_input_command.encode('utf-8'))
        #tn.write(self.__command_output_more_input_command.encode('utf-8'))
        #tn.write(self.__command_output_more_input_command.encode('utf-8'))
        #try:
            # 暴力进入sysmode，思科华为的命令都输进去，无论什么设备百分百进入。
            # 尝试登录sysmod，输入登录命令
        #    tn.write(('system-view' + "\n").encode('utf-8'))
            # 提示进入sysmod,以及输入的命令
            #print('Get in sysmod, input command:', self.__enable_command)
            # 输入enable命令
        #    tn.write((self.__enable_command + "\n").encode('utf-8'))
            # 提升权限时，区配字符，当出现'Password'时，输入密码
        #    tn.read_until(self.__password_prompt, timeout=1)
            # 提示进入sysmod输入的密码
            #print('Input enable password:', self.__enable_password)
            # 输入enable密码
        #    tn.write((self.__enable_password + '\n').encode('utf-8'))
            # 提示登录成功
            #print('Get in sysmod successfull', end='\n\n\n\n\n\n')
        #except:
        #    pass
        # 输入命令以获取网络设备的sysmodtag
        #tn.write(self.__command_output_more_input_command.encode('utf-8'))
        #tn.write(self.__command_output_more_input_command.encode('utf-8'))
        tn.write(self.__command_output_more_input_command.encode('utf-8'))
        tn.write(self.__command_output_more_input_command.encode('utf-8'))
        # 等1秒待命令输出
        time.sleep(0.5)
        sysmodtag = ((tn.read_very_eager()).decode('utf-8')[-1]).encode('utf-8')
        tn.write(self.__command_output_more_input_command.encode('utf-8'))
        # 提示输入的命令
        print('Input command:', self.__command_input)
        # 输入命令
        tn.write((self.__command_input + '\n').encode('utf-8'))
        # 将输入命令的返回值赋值response,命令返回值前两个输出不是期望的返回值而是空值
        response = tn.read_very_eager()
        #print(response)
        # 将输入命令的返回值赋值response，如果sysmodtag在response则表示命令输出完整，否则输入命令获取完整的命令
        if sysmodtag not in response:
            n = 1
            while sysmodtag not in response:
                # range(2)里面这个2是有讲究的不能少于1最好是2
                for i in range(2):
                    # 命令返回值未完结时，输入继续输出命令获取值的命令
                    tn.write(self.__command_output_more_input_command.encode('utf-8'))
                    # 获取命令返回值并赋值给response， 用response捕获命令结束提示
                    response = tn.read_until(self.__command_output_more_tag_prompt, timeout=0.5)
                    # 将获取命令返回值赋值给response_format
                    response_format = response
                    # 将response_format重新编码
                    response_format = response_format.decode('utf-8')
                    # print(response_format)
                    # 将response_format格式化
                    response_format = re.sub(r'-- \x08.*\x08', '', response_format)
                    response_format = re.sub(r'          ', '', response_format)
                    response_format = re.sub(r'\s*.*16D', '', response_format)
                    response_format = re.sub(r' ----', '', response_format)
                    response_format = re.split(r'\r\n', response_format)
                    # 删除命令的返回值中对于的无效返回值
                    for item in response_format:
                        if self.__command_output_more_tag_prompt.decode('utf-8') in item:
                            response_format.remove(item)
                    # 将输入命令的返回值添加到列表
                    for item in response_format:
                        print(item)
                        self.__command_output_list.append(item)
                    # 提示正在获取命令返回值
                    # print(response_format)
                    # print('Getting command output, please wait.',  n, 'lines command output had gotten.')
                    n = n + 1
            # 获取完整的命令输出后提示完成
            # print(hostname)
            print('All command output had gotten!!!')
        # 这些代码没用了，但是先留着可能有用
        else:
            print(2229)
            response_format = response
            print(response_format)
            response_format = response_format.decode('utf-8')
            response_format = re.split(r'\r\n', response_format)
            for item in response_format:
                print(item)
        # 这些代码没用了，但是先留着可能有用
        # 删除无效的多余的非命令返回值
        for item in self.__command_output_list:
            if self.__command_output_more_tag_prompt.decode('utf-8') in item:
                self.__command_output_list.remove(item)
        return self.__command_output_list

