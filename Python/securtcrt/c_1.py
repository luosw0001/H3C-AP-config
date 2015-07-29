# $language = "python"
# $interface = "1.0"


import os


def main():

	crt.Screen.Synchronous = True
	#开启同步，防止信息丢失
	crt.Screen.Send("show arp\r")
	#发送命令

	def k():
            while crt.Screen.WaitForString("--More--", 1) == True:
                    #循环条件crt.Screen.WaitForString里面的timeout参数1是用来当最后一行命令输出不再触发循环条件时，终止循环。

                    filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
                    fp = open(filename, "a")
                    #打开文件


                    screenrow = crt.Screen.CurrentRow - 1
                    result = crt.Screen.Get2(1, 1, screenrow, 140)
                    #获取命令输出，获取初始的那一行到光标的上一行的命令输出，get2命令获取原有格式的命令输出。


                    fp.write(result)
                    fp.close()
                    #写入文件
                    crt.Screen.Send(chr(13))
                    #输入Enter键继续下一行命令输出


        k()
        #执行程序


        filename = os.path.join('C:\Users\TIW\Desktop', 'output.txt')
        fp = open(filename, "a")
        screenrow = crt.Screen.CurrentRow - 1
        result = crt.Screen.Get2(screenrow, 1, screenrow, 140)
        fp.write(result)
        fp.close()
        crt.Screen.Send(chr(13))
        #由于最后一行触发不了循环条件，要另外加一道程序获取最后一行命令输出。

        crt.Screen.Synchronous = False
        #关闭同步



main()