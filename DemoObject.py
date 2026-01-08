class Instrument:
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        print("Strumming guitar chords")

class Piano(Instrument):
    def play(self):
        print("Playing paino melody")

class Drum(Instrument):
    def play(self):
        print("Beating drum rhythm") 

list_instrument= [Guitar(), Piano(),Drum()]
for i in list_instrument:
    i.play()