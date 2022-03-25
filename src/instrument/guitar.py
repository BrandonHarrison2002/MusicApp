from instrument.instrument import *

class guitar(instrument):
    def __init__(self):
        # super().__init__(self)
        self.name = "guitar"
        self.midi = None
        self.notes = {
            'A':57,
            'ASHARP':58,
            'B':59,
            'C':60,
            'CSHARP':61,
            'D':62,
            'DSHARP':63,
            'E':64,
            'F':65,
            'FSHARP':66,
            'G':67,
            'GSHARP':68,
        }



    