import sys

CONSTANTA = 123
some_value = 2


class SomeClass:
    pass


def f():
    return (
        1 == 2 and 2 == 3 and 1 == 2 and
            2 == 3 and 1 == 2 and 2 == 3 and
                1 == 2 and 2 == 3
    )


def f2():
    pass


if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]

    print(a, b)