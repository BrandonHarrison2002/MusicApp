#https://github.com/mido/mido/
#(MIDI) MUSICAL INSTRUMENT DIGITAL INTERFACE

import sys
from instrument import instrument

def main():
    guitar = instrument("Guitar")
    guitar.addsong("CantStop.mid") #sys.argv[1]
    print(guitar.song.gettempo())


    # with open("song.json", "w") as out:
    #     out.write(guitar.song.tojson())


if __name__ == "__main__":
    main()