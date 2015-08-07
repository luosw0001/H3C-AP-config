__author__ = 'TIW'

# coding = utf-8
import telnetlib
import re
import time


class login(object):
    def __init__(self, Host, Port, Username, Password, UsermodTag=b'>', SysmodTag=b'#', login_prompt=b'Username', password_prompt=b'Password'):
        self.host = Host
        self.port = Port
        self.username = Username
        self.password = Password
        self.usermodtag = UsermodTag
        self.sysmodtag = SysmodTag
        self.login_prompt = login_prompt
        self.password_prompt = password_prompt

