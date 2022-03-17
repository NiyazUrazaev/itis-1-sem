a = [36366, 238]
d = {
    'key1': 12
}

b = 123


def func_test(value, array=[]):
    """Bad default value"""
    array.append(value)
    return array


def func_test2(value, digit=2):
    return digit * value


print(func_test2(2))
print(func_test2(2, 3))
print(func_test2(2))

print(func_test(1, []))
print(func_test(2))
print(func_test(123))
print(func_test(3, []))