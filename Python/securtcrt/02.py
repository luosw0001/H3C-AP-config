
# $language = "python"
# $interface = "1.0"

import sys
sys.setrecursionlimit(15000)   #修改递归次数

import os

crt.Screen.Synchronous = True

crt.Screen.Send("show arp\r")





def k():
    while crt.Screen.WaitForString("--More--", 1) == True:
        a = crt.Screen.ReadString(['--More--', 'Internet'])
        a = a[27:]
        filename = os.path.join('C:\Users\TIW\Desktop', 'output2.txt')
        fp = open(filename, "a")

        #screenrow = crt.Screen.CurrentRow - 1
        #result = crt.Screen.Get(1, 1, screenrow, 140)
        fp.write(a)
        fp.close()
        crt.Screen.Send(chr(13))




def l():
    k()
    filename = os.path.join('C:\Users\TIW\Desktop', 'output2.txt')
    fp = open(filename, "a")
    screenrow = crt.Screen.CurrentRow - 1
    result = crt.Screen.Get(screenrow, 1, screenrow, 140)
    fp.write(a)
    fp.close()
    crt.Screen.Send(chr(13))


l()


crt.Screen.Synchronous = False