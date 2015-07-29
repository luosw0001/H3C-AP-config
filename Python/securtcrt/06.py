# $language = "python"
# $interface = "1.0"

import os

crt.Screen.Synchronous = True
crt.Screen.Send("show arp\r")

index = crt.Screen.MatchIndex

szOutput = crt.Screen.ReadString(["--More--", "#"])

crt.Dialog.MessageBox("ssss!")





if (index == 0):
    crt.Dialog.MessageBox("Timed out!")

elif (index == 1):
    crt.Dialog.MessageBox("--More--")

elif (index == 2):
    crt.Dialog.MessageBox("#")
    a = crt.Screen.ReadString('#', 1)
    crt.Dialog.MessageBox(str(a))
    #b = a.find('Internet')
    #a = a[b:]
    #crt.Dialog.MessageBox(a)
    #filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    #fp = open(filename, "a")
    #fp.write(a)
    #fp.close()
    #crt.Screen.Send(chr(13))


crt.Screen.Synchronous = False



