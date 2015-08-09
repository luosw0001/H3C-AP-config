__author__ = 'TIW'

# coding = utf-8
import telnetlib
import re
import time


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
command_input = 'show run'



###########################登录步骤######################################
def login():
    ###实例化telnet对象，建立一个主机连接
    tn = telnetlib.Telnet(host, port=port, timeout=50000)
    # 开启调试，按需开启，方便判断
    #telnetsession.set_debuglevel(2)
    # 区配字符，当出现'Username'时，输入用户名
    tn.read_until(login_prompt)
    # 提示输入的用户名
    print('Input Username:', username)
    # 输入用户名
    tn.write((username + '\n').encode('utf-8'))
    print(1)
    print(tn.read_very_eager())
    # 区配字符，当出现'Password'时，输入密码
    tn.read_until(password_prompt)
    # 提示输入的密码
    print('Input Password:', password)
    # 输入密码
    tn.write((password + '\n').encode('utf-8'))
    print(2)
    print(tn.read_very_eager())
    # 如果登录Usermode成功，则出现类似>,使用UsermodTag来进行捕获
    tn.read_until(usermodtag)
    print('Get in stsmod, input command:', enable_command)
    tn.write((enable_command + "\n").encode('utf-8'))
    print(3)
    print(tn.read_very_eager())
    # 提升权限时，区配字符，当出现'Password'时，输入密码
    tn.read_until(b'Password')
    # 提示进入sysmod输入的密码
    print('Input sysmod password:', enable_password)
    tn.write((enable_password + '\n').encode('utf-8'))
    print(4)
    print(tn.read_very_eager())
    # 如果登录Sysmode成功，则出现类似#,使用SysmodTag来进行捕获
    tn.read_until(sysmodtag)
    tn.write((command_input + '\n').encode('utf-8'))
    print(5)
    response = tn.read_until(b'More')
    n = 5
    if b'#' not in response:
        while b'#' not in response:
            n = n + 1
            print('########')
            print(n)
            for i in range(2):
                tn.write(command_output_more_input_command.encode('utf-8'))
                response = tn.read_until(command_output_more_tag_prompt, timeout=0.5)
                print(response)
            time.sleep(0.01)
        print(777777777777777777777777777777777777777777)
    else:
        pass
    tn.close()
    print('########fuck############')

###########################登录步骤######################################

login()
