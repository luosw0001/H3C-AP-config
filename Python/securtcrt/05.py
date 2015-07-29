# $language = "python"
# $interface = "1.0"





import os

crt.Screen.Synchronous = True
crt.Screen.Send("show arp\r")

c = crt.Screen.WaitForStrings(['#', '--More--'], 1)

if (c == 1):
    crt.Dialog.MessageBox('#')
    a = crt.Screen.ReadString('#', 1)
    crt.Dialog.MessageBox(str(a))
    b = a.find('Internet')
    a = a[b:]
    crt.Dialog.MessageBox(str(a))
    filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    fp = open(filename, "a")
    fp.write(a)
    fp.close()
    crt.Screen.Send(chr(13))

elif (c == 2):
    crt.Dialog.MessageBox('shitX')

    a = crt.Screen.ReadString('--More--', 1)
    b = a.find('Internet')
    a = a[b:]
    filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    fp = open(filename, "a")
    fp.write(a)
    fp.close()
    crt.Screen.Send(chr(13))
    def g():

        crt.Dialog.MessageBox('shit1')

        while crt.Screen.WaitForString("--More--", 1):

            crt.Dialog.MessageBox('shit2')
            a = crt.Screen.ReadString('--More--', 1)
            b = a.find('Internet')
            a = a[b:]
            filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
            fp = open(filename, "a")
            fp.write(a)
            fp.close()
            crt.Screen.Send(chr(13))

    g()

    crt.Dialog.MessageBox('shit3')
    #filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    #fp = open(filename, "a")
    #screenrow = crt.Screen.CurrentRow - 1
    #result = crt.Screen.Get2(screenrow, 1, screenrow, 140)
    #fp.write(result)
    #fp.close()



crt.Screen.Synchronous = False
