class Note:
    sound = ""
    long = False

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
            return self.sound + "-" + self.sound[len(self.sound) - 1]
