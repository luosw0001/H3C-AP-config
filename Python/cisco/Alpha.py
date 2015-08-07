__author__ = 'TIW'
#coding=utf-8
#http://support.huawei.com/ecommunity/bbs/10173767.html
#http://www.jbxue.com/article/32063.html
import telnetlib
import re
import time


### 配置登录信息
Username = 'cisco'
Password = 'cisco'
Host = '10.0.0.1'
Port = '23'
UsermodTag = b'>'
SysrmodTag = b'#'
login_prompt = [b'Username']
password_prompt = b'*Password'


###实例化telnet对象，建立一个主机连接
tn = telnetlib.Telnet(Host)
# 开启调试，按需开启，方便判断
#telnetsession.set_debuglevel(2)
# 区配字符，当出现'Username'时，输入用户名
if tn.expect(login_prompt):
    #print response
    print('Input Username:', Username)
    tn.write(Username + '\n')
    time.sleep(1)
# 区配字符，当出现'Password'时，输入密码
if tn.expect(re.match(password_prompt)):
    #print response
    print('Input Password:', Password)
    tn.write(Password + '\n')
    time.sleep(1)
# 如果登录成功，则出现类似>,使用UsermodTag来进行捕获
if tn.expect(re.match(UsermodTag)):
    #print response
    print('In Usermod, be going to get in sysmod')
    tn.write(b'en' + '\n')
    time.sleep(1)
# 提升权限时，区配字符，当出现'Password'时，输入密码
password_prompt = b'Password'
if tn.expect(re.match(password_prompt)):
    #print response
    print('Input Password:', Password)
    tn.write(Password + '\n')
    time.sleep(1)
# 如果认证成功，则出现类似#,使用SysrmodTag来进行捕获
if tn.expect(re.match(SysrmodTag)):
    #print response
    print('In Sysmod, input command')
    tn.write(b'show run' + '\n')
    time.sleep(3)
    print(tn.read_until(SysrmodTag))
    time.sleep(2)
telnetsession.close()
print('[*] Session Close.')




