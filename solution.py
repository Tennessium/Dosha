PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    sound = ""
    is_long = False
    dick = {
        "до": "до-о",
        "ре": "ре-э",
        "ми": "ми-и",
        "фа": "фа-а",
        "соль": "со-оль",
        "ля": "ля-а",
        "си": "си-и"
    }

    def __init__(self, sound="до", is_long=False):
        self.sound = sound
        self.is_long = is_long

    def __str__(self):
        if not self.is_long:
            return self.sound
        else:
            return self.dick[self.sound]


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, sound="до", is_long=False):
        super().__init__(sound, is_long)

    def __str__(self):
        return super().__str__()


class NoteWithOctave(Note):
    octava = ""

    def __init__(self, sound, octava="", is_long=False):
        super().__init__(sound, is_long)
        self.octava = octava

    def __str__(self):
        return super().__str__() + " (" + self.octava + ')'
