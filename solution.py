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


class ColoredPoint(Point):
    color = (0, 0, 0)

    def __init__(self, name, x, y, color=(0, 0, 0)):
        self.color = color
        super().__init__(name, x, y)

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, (255 - self.color[0], 255 - self.color[1], 255 - self.color[2]))

    def get_color(self):
        return self.color

    #def __str__(self):
    #    return super().__str__() + " " + str(self.color)
