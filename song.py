import mido, json

class song(mido.MidiFile):
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