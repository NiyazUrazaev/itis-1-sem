def func_pow(a):
    return a ** 2


def sort_by_key(a: int):
    return a % 2 == 0


array = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(func_pow, array)))

print(list(filter(sort_by_key, array)))

print('!!!Lambda!!!')

func = lambda a: a ** 2
print(list(map(lambda a: a ** 2, array)))
print(list(map(func, array)))

print(list(filter(lambda a: a % 2 == 0, array)))







