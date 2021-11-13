def some_func():
    return 2


class SomeClass(object):
    a = 1

    def __init__(self, b, c, d):
        self.b = b
        self.c = c
        self.d = d

    def some_func(self):
        return self.a

    def some_func2(self):
        return self.some_func()

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def __str__(self):
        s = f'{self.a}'
        s2 = '{a}'.format(a=1)
        return f'A: {self.a}, b: {self.b}'


s = SomeClass(2, 3, 4)

print(str(s))