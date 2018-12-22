class Point:
    x = 0
    y = 0
    name = ''

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.get_x(), self.get_y())

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __str__(self):
        return self.name + str(self.get_coords())
