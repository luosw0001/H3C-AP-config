__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

a = r'\s*(Eth|GE|GI|FastEthernet)\s*'
b = ['', '[H3C_7F2626_1]display poe interface ', ' Interface    Status   Priority CurPower Operating  IEEE   Detection', '                                (W)      Status     Class  Status', ' Eth1/0/1     enabled  low      2.3      on         3      delivering-power', ' Eth1/0/2     enabled  low      2.3      on         3      delivering-power', ' Eth1/0/3     enabled  low      7.0      on         3      delivering-power', ' Eth1/0/4     enabled  low      2.5      on         3      delivering-power', ' Eth1/0/5     enabled  low      2.5      on         3      delivering-power', ' Eth1/0/6     enabled  low      5.5      on         3      delivering-power', ' Eth1/0/7     enabled  low      2.5      on         3      delivering-power', ' Eth1/0/8     enabled  low      2.3      on         3      delivering-power', ' Eth1/0/9     enabled  low      2.5      on         3      delivering-power', ' Eth1/0/10    enabled  low      2.5      on         3      delivering-power', ' Eth1/0/11    enabled  low      2.5      on         3      delivering-power', ' Eth1/0/12    enabled  low      2.3      on         3      delivering-power', ' Eth1/0/13    enabled  low      2.4      on         3      delivering-power', ' Eth1/0/14    enabled  low      2.4      on         3      delivering-power', ' Eth1/0/15    enabled  low      5.3      on         3      delivering-power', ' Eth1/0/16    enabled  low      0.0      off        0      searching', ' Eth1/0/17    enabled  low      0.0      off        0      searching', ' Eth1/0/18    enabled  low      0.0      off        0      searching', ' Eth1/0/19    enabled  low      0.0      off        0      searching', ' Eth1/0/20    enabled  low      0.0      off        0      searching', ' Eth1/0/21    enabled  low      0.0      off        0      searching', ' Eth1/0/22    enabled  low      0.0      off        0      searching', ' Eth1/0/23    enabled  low      0.0      off        0      searching', ' Eth1/0/24    enabled  low      0.0      off        0      searching', '   ---  15 port(s) on,    46.8 (W) consumed,   143.2 (W) remaining ---', '', '[H3C_7F2626_1]', '[H3C_7F2626_1]']

def match(a, b):
    if re.match(a, b):
        print(b)

for item in b:
    match(a, item)
