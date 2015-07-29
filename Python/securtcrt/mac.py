# $language = "python"
# $interface = "1.0"

# $coding = "GBK"
# exConnectToSessionsAndSendCommands3.py
#
# Description:
#     Reads in sessions from a file (one session per line) and
#     connects to each one (one at a time) and sends a series of
#     commands to the remote, then disconnects from the session
#     and moves on to the next session.
#     
#     By default, the file containing the sessions is expected to be named
#     "SessionList.txt", and should be located in the current 
#     folder.  Each line of the file is expected to contain the
#     path to the session as it appears within the Connect dialog (excluding
#     the leading "Sessions/" component.  Here is an example file contents:
#         
#         redhat
#         redhat8
#         192.168.0.123
#         192.168.0.131
#         Redhat Sessions\RedHat - XTerm
#
#     For the sake of simplicity, this example assumes that all
#     sessions we're connecting to are using the SSH1 and SSH2
#     protocols, with usernames and passwords saved encrypted
#     as part of the session configuration so that we don't need
#     to worry about authentication within this script.
#

# Using GetScriptTab() will make this script 'tab safe' in that all of the
# script's functionality will be carried out on the correct tab. From here
# on out we'll use the SCRIPT_TAB object instead of the crt object.


import os
import sys

from subprocess import *

# Be "tab safe" by getting a reference to the tab for which this script
# has been launched:
SCRIPT_TAB = crt.GetScriptTab()
SCRIPT_TAB.Screen.Synchronous = True

g_szErrors = ""

def main():
    global g_szErrors
    szData = ""
    
    # Read in Sessions from a file that contains session names (paths as they
    # appear in the Connect dialog), one per line
    sessions = []
    with open("SessionList3.txt") as f:
      for line in f:
        line = line.strip()
        if line:
          sessions.append(line)

    fp = file("temp.txt", "w")

    # Connect to each session and issue a few commands, then disconnect.
    for line in sessions:
      try:
        crt.Session.Connect("/S " + chr(34) + line + chr(34))
      except Exception as e:        
        szError = str(e)
        
      # If we successfully connected, we'll do the work we intend to do...
      # otherwise, we'll skip the work and move on to the next session in 
      # the list.
      if crt.Session.Connected:
          crt.Screen.Synchronous = True
          
          # When we first connect, there will likely be data arriving from the
          # remote system.  This is one way of detecting when it's safe to
          # start sending data.
          while crt.Screen.WaitForCursor(1):
            pass
          # Once the cursor has stopped moving for about a second, we'll
          # assume it's safe to start interacting with the remote system.
          
          # Get the shell prompt so that we can know what to look for when
          # determining if the command is completed. Won't work if the prompt
          # is dynamic (e.g. changes according to current working folder, etc)
          nRow = crt.Screen.CurrentRow
          szPrompt = crt.Screen.Get(nRow,0,nRow,crt.Screen.CurrentColumn-1)
          szPrompt = szPrompt.strip()
          
          WriteData2(fp, "\n===========================================================\n")
          WriteData2(fp, szPrompt[:-1])
          WriteData2(fp, "\n==========================\n")
          WriteData2(fp, CaptureOutputOfCommand("show mac-addr", szPrompt)+"\n")
          WriteData2(fp, CaptureOutputOfCommand("disp mac-addr", szPrompt)+"\n")

          # Now disconnect from the remote machine...
          crt.Session.Disconnect()
          # Wait for the connection to close
          while crt.Session.Connected:
              crt.Sleep(100)
       
          crt.Sleep(1000)
      else:
          g_szErrors += "\n*** Error connecting to " + line + ": " + szError
    
    fp.close()
    #crt.Clipboard.Format = "CF_TEXT"
    #crt.Clipboard.Text = szData
    
    if not g_szErrors:
        crt.Dialog.MessageBox("Tasks completed.  No Errors were detected.")
    else:
        crt.Dialog.MessageBox("Tasks completed.  The following errors occurred:\n" +
            vbcrlf & g_szErrors)

def SendExpect(szSend, szExpect):
    # Returns true if the text in 'szSend' was successfully sent and
    # the text in 'szExpect' was successfully found as a result.

    # If we're not connected, we can't possibly return true, or even send/recv
    # text
    if not SCRIPT_TAB.Session.Connected:
      return(False)
        
    SCRIPT_TAB.Screen.Send(szSend + "\r")
    SCRIPT_TAB.Screen.WaitForString(szExpect)

    return(True)


def CaptureOutputOfCommand(szCommand, szPrompt):
    if not crt.Session.Connected:
        return("[ERROR: Not Connected.]")
    
    # First, send the command to the remote.
    SCRIPT_TAB.Screen.Send(szCommand  + "\r")
    
    # Second, wait for the carriage return to be echoed by the remote device.
    # This allows us to capture only the output of the command, not the line
    # on which the command was issued (which would include the prompt + cmd).
    # If you want to capture the command that was issued, simply comment out
    # the following line of code.
    #SCRIPT_TAB.Screen.WaitForString("\r")
    
    # Now that the command has been sent, use Screen.ReadString to capture
    # all the data that is received up to the point at which the shell
    # prompt appears (the captured data does not include the shell prompt).
    szData = ""
    while True:
      line = crt.Screen.ReadString([szPrompt, "ore--", "ore ----"],1000)
      if line[-3:]=="--M":
        szData += line[:-3]
        SCRIPT_TAB.Screen.Send(" ")
        SCRIPT_TAB.Screen.WaitForString(" "*6+"\x08"*9+" ", 10)
      elif line[-8:]=="  ---- M":
        szData += line[:-8]
        SCRIPT_TAB.Screen.Send(" ")
        SCRIPT_TAB.Screen.WaitForString(" "*30+"\x1B[42D", 10)
      else:
        szData += line
        break

    return(szData)

def WriteData2(fp, text):
    for line in text.splitlines():
      fp.write(line + os.linesep)
      

main()
