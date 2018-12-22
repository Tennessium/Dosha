class BellTower:
    kolokola = []

    def __init__(self, *args):
        for i in args:
            self.kolokola.append(i)

    def append(self, x):
        self.kolokola.append(x)
        for i in self.kolokola:
            i.ding = True

    def sound(self):
        for i in self.kolokola:
            i.sound()
        print("...")


class LittleBell:
    ding = True
    
    def __init__(self):
        pass

    def sound(self):
        print("ding")


class BigBell:
    ding = True

    def __init__(self):
        pass

    def sound(self):
        if self.ding:
            print("ding")
        else:
            print("dong")
        self.ding = not self.ding
