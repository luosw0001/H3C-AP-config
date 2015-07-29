
# $language = "python"
# $interface = "1.0"


import os

import os

crt.Screen.Synchronous = True



def g():

    screenrow = crt.Screen.CurrentRow - 1
    result = crt.Screen.Get(screenrow, 1, screenrow, 140)
    filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
    fp = open(filename, "a")
    fp.write(result)
    fp.close()


#g()

#if crt.Screen.WaitForCursor(10):
#    crt.Dialog.MessageBox('oooooo!!!')

#crt.Screen.WaitForString("Traceback")
#crt.Dialog.MessageBox('Shit!!!')

screenrow = crt.Screen.CurrentRow
result = crt.Screen.Get(screenrow, 1, screenrow, 140)

if result == '':
    crt.Dialog.MessageBox('oooooo!!!')

crt.Screen.Synchronous = False