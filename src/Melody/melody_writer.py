from music21 import stream, midi
from NoteFactory import new_note as n
import matplotlib
import numpy

out_dir = "./out/"


def export_midi(filename: str, export_stream: stream.Stream) -> None:
    mf = midi.translate.streamToMidiFile(export_stream)
    mf.open(out_dir + filename + '.mid', 'wb')
    mf.write()
    mf.close()


def generate_default() -> None:
    s = stream.Stream()
    s.append([n("C4"), n("C4"), n("G4"), n("G4"), n("A4"), n("A4"), n("G4", 2)])
    export_midi("melody", s)
