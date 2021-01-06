from music21 import note


def new_note(note_id: str, length=1) -> note.Note:
    return note.Note(note_id, quarterNotes=length)
