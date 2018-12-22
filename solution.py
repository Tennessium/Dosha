class BellTower:
    kolokola = []

    def __init__(self, *args):
        for i in args:
            self.kolokola.append(i)

    def append(self, x):
        self.kolokola.append(x)

    def sound(self):
        for i in self.kolokola:
            i.sound()
        print("...")


class Bell:
    def __init__(self, *args):
        self.data = []
        self.kdata = {}

        for i in args:
            if isinstance(i, str):
                self.data.append(i)
            elif isinstance(i, dict):
                for j in i:
                    self.kdata[j] = i[j]
            elif isinstance(i, tuple):
                for j in i:
                    if isinstance(j, str):
                        self.data.append(j)

    def print_info(self):
        s = ""
        self.data.sort()
        keys = self.kdata.keys()
        dd = []
        for i in keys:
            dd.append(i)

        dd.sort()

        for i in dd:
            s += i + ': ' + self.kdata[i] + ', '
        try:
            s = s[:-2]
        except Exception:
            pass
        if len(s) != 0:
            s += '; '
        for i in self.data:
            s += i + ', '
        try:
            s = s[:-2]
        except Exception:
            pass
        if s == "":
            print('-')
        else:
            print(s)


class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def sound(self):
        print("ding")


class BigBell(Bell):
    ding = True

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def sound(self):
        if self.ding:
            print("ding")
        else:
            print("dong")
        self.ding = not self.ding
