n = int(input())

summa = 1
k = 3

for i in range(1, n):
    summa += ((-1) ** i) * 1 / (k ** 2)
    k += 2

print(summa)
