import socket
from PyNTR import PyNTR
import time
import os

# ------ CONFIG START ------
myIP = '192.168.1.8' # the 3DS IP address
game = 'usum' # UltraSun/UltraMoon
#game = 'sm'   # Sun/Moon
# ------- CONFIG END -------

# PyHeX is a Python3 command-line script made by YoshiOG.  It is used for 
# cloning Pokemon in Gen 7 games on-the-fly using NTR CFW.

# Credits:
#  - imthe666st : Wrote PyNTR, which this script depends on
#    - https://github.com/imthe666st/PyNTR
#  - Cell9 : Created NTR CFW
#  - YoshiOG : Created this script

# You may redistribute this script, just don't claim this as your work!

client = PyNTR.PyNTR(myIP)
client.start_connection()
client.send_hello_packet()
if game.lower() == 'usum':
    client.set_game_name('momiji')
    boxOffset = 0x33015AB0
if game.lower() == 'sm' or game.lower() == 'sumo':
    client.set_game_name('niji_loc')
    boxOffset = 0x330D9838

print("PyHeX by YoshiOG.  Please use responsibly; I am not responsible for any data loss, bans, etc.")
print("Currently implemented commands:")
print(" clone(sourceBox, sourceSlot, copies[, destBox, destSlot])\n   Clones the Pokemon from source box/slot N times to destination box/slot.  Default destination is set to source.")
print(" boxexport(box[, filepath])\n  Dumps all Pokemon data from given box to an EK7 binary.  Default filepath is 'boxdump.ek7' in the folder PyHeX is in.")
print(" boximport(box[, filepath])\n  Overwrites all Pokemon data in given box with data from an EK7 box binary.  Imports from 'boxdump.ek7' by default.")

def clone(sourceBox = 255, sourceSlot = 255, copies = 0, destBox = 0, destSlot = 0):
    if sourceBox == 255 or sourceSlot == 255 or copies == 0:
        print('Please specify a box/slot and number of copies (at least 1)')
        return
    if sourceBox > 32 and sourceBox != 255:
        print('Box number must be between 1-32!')
        return
    if sourceSlot > 30 or sourceSlot == 0:
        print('Slot number must be between 1-30!')
        return
    if destBox > 32:
        print('Box number must be between 1-32!')
        return
    if destSlot > 30:
        print('Slot number must be between 1-30!')
        return
    sourceOff = boxOffset + (0xE8 * (sourceSlot - 1)) + (0x1B30 * (sourceBox - 1))
    destOff = sourceOff
    if destSlot != 0:
        destOff = boxOffset + (0xE8 * (destSlot - 1)) + (0x1B30 * (destBox - 1))
    if destSlot == 0:
        destBox = sourceBox
        destSlot = sourceSlot
    
    print('Reading PKM at Box ' + str(sourceBox) + ', Slot ' + str(sourceSlot))
    sourcePkm = client.ReadCustom(sourceOff, 0xE8)
    print('Writing ' + str(copies) + ' copies starting at Box ' + str(destBox) + ', Slot ' + str(destSlot))
    for x in range(0, copies):
        client.WriteCustom(0xE8 * x + destOff, sourcePkm, 0xE8)
    
    print('Cloning complete!')

def boxexport(box = 0, dumpPath = './boxdump.ek7'):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    dumpOffset = 0x1B30 * (box - 1) + boxOffset
    print('Reading raw data from Box ' + str(box))
    dumpPkm = client.ReadCustom(dumpOffset, 0x1B30)
    f = open(dumpPath, 'wb+')
    f.write(dumpPkm.to_bytes(0x1B30, 'little'))
    f.close()
    print('Box ' + str(box) + ' dumped to ' + dumpPath)

def boximport(box = 0, thePath = './boxdump.ek7'):
    if box > 32 or box < 1:
        print('Box number must be between 1-32!')
        return
    importOff = 0x1B30 * (box - 1) + boxOffset
    print('Writing raw box data to Box ' + str(box))
    if not os.path.exists(thePath):
        print("The file could not be found.  Try boxexport() to create a dump!")
    f = open(thePath, 'rb+')
    content = f.read()
    client.WriteCustom(importOff, content, 0x1B30)
    f.close()
    print('Data from ' + str(thePath) + ' written to Box ' + str(box))


while 1:
    eval(input("<PyHex> "))