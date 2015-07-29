# $language = "python"
# $interface = "1.0"

import sys
sys.setrecursionlimit(15000)   #修改递归次数


import os

crt.Screen.Synchronous = True
crt.Screen.Send("show arp\r")



def k():

    a = crt.Screen.ReadString('--More--')
    b = a.find('Internet')
    a = a[b:]

    #crt.Dialog.MessageBox(str(a))
    filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    fp = open(filename, "a")
    
    #screenrow = crt.Screen.CurrentRow - 1
    #result = crt.Screen.Get(1, 1, screenrow, 140)
    fp.write(a)
    fp.close()
    crt.Screen.Send(chr(13))
    k()


k()





def g():

    screenrow = crt.Screen.CurrentRow - 1
    result = crt.Screen.Get(screenrow, 1, screenrow, 140)
    filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    fp = open(filename, "a")
    fp.write(result)
    fp.close()





crt.Screen.Synchronous = False    


