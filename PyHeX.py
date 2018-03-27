# PyHeX is a Python3 command-line script made by YoshiOG.  It is used for 
# cloning Pokemon in Gen 7 games on-the-fly using NTR CFW.

# Credits:
#  - imthe666st : Wrote PyNTR, which this script depends on
#    - https://github.com/imthe666st/PyNTR
#  - Cell9 : Created NTR CFW
#  - YoshiOG : Created this script

# You may redistribute this script, just don't claim this as your work!
import socket
from PyNTR import PyNTR
import time
import os
import random
import array
import binascii
import sys

# ------ CONFIG START ------
myIP = '192.168.1.3' # the 3DS IP address
game = 'usum' # UltraSun/UltraMoon
#game = 'sm'   # Sun/Moon
# ------- CONFIG END -------

if len(sys.argv) >= 3:
    myIP = sys.argv[1]
    game = sys.argv[2]

from PyHeXcore import *
print("PyHeX by YoshiOG.  Please use responsibly; I am not responsible for any data loss, bans, etc.")
print("For syntax of commands, type 'cmdhelp'")
print("To input a command from this prompt, use this format:\n    command arg1 arg2 ...")
print("For example, this fills Box 1 with all PK7s from MyFolder, in random order:\n<PyHeX-example> dirimport 1,'./MyFolder',True\n\n")
while 1:
    theInput = input("<PyHex> ")
    if theInput != "":
        theArray = theInput.split(" ")
        theCmd = theInput.split(" ")[0]
        theArgs = ""
        if len(theArray) > 1:
            theArgs = theInput.replace(theCmd + " ","").replace("\\","\\\\")
        eval(theCmd + "(" + theArgs + ")")