__author__ = 'TIW'



from telnetlib import Telnet
tn = Telnet('10.0.0.1')
tn.read_until('Username:'.encode('ascii'))
tn.write('cisco'.encode('ascii') + b"\n")
tn.write('cisco'.encode('ascii') + b"\n")
tn.read_until('en:'.encode('ascii') + b"\n")
tn.write('cisco'.encode('ascii') + b"\n")
tn.write('show run'.encode('ascii') + b"\n")
print(tn.read_all())
tn.close()
