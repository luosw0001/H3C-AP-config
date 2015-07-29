# $language = "Python"
# $interface = "1.0"

# Connect to a telnet server and automate the initial login sequence.
# Note that synchronous mode is enabled to prevent server output from
# potentially being missed.



def main(n):

	crt.Screen.Synchronous = True

	# connect to host on port 23 (the default telnet port)
	#
	crt.Screen.Send("telnet " + str(n) + "\r")

	# telnet目的设备

	crt.Screen.WaitForString("Username:")
	crt.Screen.Send("cisco\r")

	# 待提示输入账号之后输入账号

	crt.Screen.WaitForString("Password:")
	crt.Screen.Send("cisco\r")

	#待提示输入密码之后输入密码

	crt.Screen.WaitForString(">")
	crt.Screen.Send("enable\r")

	#待提示?模式之后进入特权模式

	crt.Screen.WaitForString("Password:")
	crt.Screen.Send("cisco\r")

	#待提示特权模式密码之后输入密码

	crt.Screen.Synchronous = False


a = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']

for i in a:
        man(i)
        crt.Screen.Synchronous = True
        crt.Screen.WaitForString("#")
	crt.Screen.Send("exit")
        crt.Screen.WaitForString(">")
	crt.Screen.Send("exit")

