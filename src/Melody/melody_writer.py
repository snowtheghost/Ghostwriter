from music21 import note, stream, midi

# music21 dependencies
import matplotlib
import numpy

# trial
if __name__ == "__main__":
    s = stream.Stream()
    s.append([note.Note("C4"), note.Note("C4"),
              note.Note("G4"), note.Note("G4"),
              note.Note("A4"), note.Note("A4"),
              note.Note("G4", quarterLength=2)])
    mf = midi.translate.streamToMidiFile(s)
    mf.open('./out/melody.mid', 'wb')
    mf.write()
    mf.close()
