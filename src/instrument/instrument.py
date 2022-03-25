import mido, json, time


class midi(mido.MidiFile):
    def __init__(self, filename=None, file=None, type=1, ticks_per_beat=480, charset='latin1', debug=False, clip=False, tracks=None):
        super().__init__(filename, file, type, ticks_per_beat, charset, debug, clip, tracks)


    def gettempo(self):
        for data in self.toarray()[0]:
            try:
                self.tempo = data['tempo']
                return data['tempo']
            except: 
                pass

    def toarray(self):
        tracks = []
        for track in self.tracks:
            tracks.append([vars(msg).copy() for msg in track])
        return tracks

    def midifile_to_dict(self):
        tracks = []
        for track in self.tracks:
            tracks.append([vars(msg).copy() for msg in track])

        return {
            'ticks_per_beat': self.ticks_per_beat,
            'tracks': tracks,
        }
    
    def tojson(self):
        return json.dumps(self.midifile_to_dict(), indent=2)


class instrument():
    def __init__(self):
        self.name = None
        self.midi = None
        self.notes = {}

    def addmidi(self, filename=None, file=None, type=1, ticks_per_beat=480, charset='latin1', debug=False, clip=False, tracks=None):
        self.midi = midi(filename, file, type, ticks_per_beat, charset, debug, clip, tracks)
        print(f"Added {self.midi.filename[:-4]}")

    def avainotes(self, arg):
        '''Note availity'''
        for note in self.notes.values():
            if arg==note: return True

        return False

    def play(self, delay=0):
        queue = []
        for msg in self.midi.play():
            time.sleep(delay)
            msg = vars(msg)
            if msg['type'] == 'note_on': #Check if note message
                if self.avainotes(msg['note']): #Check if instrument can play
                    if (msg['velocity']): #Check if it's ending notes
                        print(msg)
                    else:
                        queue.clear() 
                        print(f'\n\n')
        

