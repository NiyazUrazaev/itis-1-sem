# a = []
# for i in range(10):
#     a.append(i)
#
# b = [i if i > 2 else 1 for i in range(10)]
#
# t = (i for i in range(10))
#
# print(a, b, t)

s = ''

array = [['-'] * 10 for j in range(10)]

print(array)
# print(array[1][2])

for i in range(10):
    for j in range(10):
        if i == j:
            array[i][j] = '*'
        print(array[i][j], end=' ')
    print()