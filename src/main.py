#https://github.com/mido/mido/
#(MIDI) MUSICAL INSTRUMENT DIGITAL INTERFACE

import sys
from instrument import *


def main():
    newguitar = guitar()
    songname = "CantStop"#sys.argv[1]
    newguitar.addmidi(f"..\\lib\\{songname}.mid")
    newguitar.play()

if __name__ == "__main__":
    main()