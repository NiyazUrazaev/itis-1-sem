import random

# a = [1, 2, 3, 4]
#
# for i in a:
#     print(i)
#
# b = iter(a)
#
# for i in b:
#     print(b)


class RandomIterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            return random.randint(1, 100)
        else:
            raise StopIteration


random_iterator = RandomIterator(10)

for i in random_iterator:
    print(i)