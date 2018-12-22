class Note:
    sound = ""
    long = False
    dick = {
        "до": "до-о",
        "ре": "ре-э",
        "ми": "ми-и",
        "фа": "фа-а",
        "соль": "со-оль",
        "ля": "ля-а",
        "си": "си-и"
    }

    def __init__(self, *args):
        self.sound = args[0]
        try:
            self.long = args[1]
        except Exception:
            pass

    def __str__(self):
        if not self.long:
            return self.sound
        else:
            return self.dick[self.sound]
