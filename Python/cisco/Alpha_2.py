__author__ = 'TIW'
# coding = utf-8
import telnetlib
import re
import time

### 配置登录信息
### 网络设备IP
Host = '218.17.209.74'
### 网络设备telnet端口
Port = 60001
### 登录帐号
Username = 'admin' + '\n'
### 登录密码
Password = 'admin@123' + '\n'
### Usermode提示符
UsermodTag = b'>'
### Sysmode提示符
SysrmodTag = b'#'
### 登录网络设备时提示输入账号的提示
login_prompt = b'Username'
### 登录网络设备时提示输入密码的提示
password_prompt = b'Password'
### 输入的命令
command_input = 'show run' + "\n"




def login():
    ###实例化telnet对象，建立一个主机连接
    tn = telnetlib.Telnet(Host, port=Port, timeout=50000)
    # 开启调试，按需开启，方便判断
    #telnetsession.set_debuglevel(2)
    # 区配字符，当出现'Username'时，输入用户名
    tn.read_until(login_prompt)
    print('Input Username:', Username)
    tn.write(Username.encode('utf-8'))
    print(1)
    print(tn.read_very_eager())
    # 区配字符，当出现'Password'时，输入密码
    tn.read_until(password_prompt)
    print('Input Password:', Password)
    tn.write(Password.encode('utf-8'))
    print(2)
    #time.sleep(0.8)
    print(tn.read_very_eager())
    # 如果登录Usermode成功，则出现类似>,使用UsermodTag来进行捕获
    tn.read_until(b'>')
    print('提升权限')
    tn.write(('en' + "\n").encode('utf-8'))
    print(3)
    #time.sleep(0.8)
    print(tn.read_very_eager())
    # 提升权限时，区配字符，当出现'Password'时，输入密码
    tn.read_until(b'Password')
    print('提升权限输入密码:', Password)
    tn.write(Password.encode('utf-8'))
    print(4)
    print(tn.read_very_eager())

    tn.read_until(b'#')
    tn.write(command_input.encode('utf-8'))
    print(5)
    response = tn.read_until(b'More')
    n = 5
    if b'#' not in response:
        while b'#' not in response:
            n = n + 1
            print('########')
            print(n)

            for i in range(2):
                tn.write(('\n').encode('utf-8'))

                response = tn.read_until(b'More', timeout=0.5)

                print(response)
            time.sleep(0.01)
        print(777777777777777777777777777777777777777777)
    else:
        pass


    #print(tn.read_very_eager())

    tn.close()
    print('########fuck############')



login()
