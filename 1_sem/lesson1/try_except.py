try:
    a = 1
except ZeroDivisionError as zde:
    print(zde)
else:
    print('Else')
finally:
    print('Finally')

"""
    С помощью цикла while выполнить пробежку по итерируемому объекту. 
    Использовать метод next. 
    В случае возникновения ошибки StopIteration обработать ее
    (Создаем свой цикл for)
"""

iterator_obj = iter('abracadabra')
while True:
    try:
        print(next(iterator_obj))
    except StopIteration:
        print('It is all')
        break