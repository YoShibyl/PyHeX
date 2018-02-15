# PyHeX
PyHeX is a WIP Python 3 script for cloning Pokemon on-the-fly in Generation 7 Pokemon games via NTR CFW.  It provides a command-line interface for cloning Pokemon and dumping/injecting boxes to/from `.ek7` binary files.

**Use responsibly.  I am not responsible for any damage done to your game, or any bans from Nintendo, etc.**

## Usage
First, you'll need to download and extract the contents of this repo to your device (tested on PC/Android).

Then, modify the PyHeX.py file with a text editor and change the variables within the designated CONFIG lines appropriately.

 + I'm lazy, so I didn't feel like implementing a separate config file.  Sorry :P

Lastly, just run the PyHeX.py file like any other Python script, and clone away!

### Commands
`clone(sourceBox, sourceSlot, copies[, destBox, destSlot])`
 + Clones the Pokemon from source box/slot N times to destination box/slot.  Default destination is set to source.
`boxexport(box[, filepath])`
 + Dumps all Pokemon data from given box to an EK7 binary.  Default filepath is `boxdump.ek7` in the folder PyHeX is in.
`boximport(box[, filepath])`
 + Overwrites all Pokemon data in given box with data from an EK7 box binary.  Imports from `boxdump.ek7` by default.
