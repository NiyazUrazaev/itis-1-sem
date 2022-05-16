class FigureAbstract:
    def get_s(self):
        raise NotImplementedError


class Triangle(FigureAbstract):
    def __init__(self, h, a):
        self.h = h
        self.a = a

    def get_s(self):
        return self.h * self.a / 2


class Quadrate(FigureAbstract):
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def get_s(self):
        return self.b * self.a


def get_s(object_class):
    if isinstance(object_class, Quadrate):
        pass
    elif isinstance(object_class, Triangle):
        pass
    return object_class.get_s()


q = Quadrate(3, 3)
t = Triangle(3, 2)

print(get_s(q))
print(get_s(t))