import random


def decrease_mana(attack):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def wrapper(cat1, cat2):
        print('До атаки:', cat2.name, cat2.hp)
        attack(cat1, cat2) # Сама функция
        print('После атаки:', cat2.name, cat2.hp)
    # Вернём эту функцию
    return wrapper


class Cat:
    def __init__(self, name, damag, mana, hp=100):
        self.name = name
        self.damag = damag
        self.mana = mana
        self.hp = hp

    @decrease_mana
    def attack(self, cat2):
        crit = Cat.get_crit(1, 100)
        cat2.hp -= self.damag * crit

    @staticmethod
    def get_crit(a, b):
        random_number = random.randint(a, b)
        crit = 1
        if random_number > 50:
            print('Выпал крит')
            crit = 2
        else:
            print('Крит не выпал')
        return crit


cat1 = Cat('Cat1', damag=50, mana=10)
cat2 = Cat('Cat2', 2, 5, 200)

cat1.attack(cat2)

# cat1.get_crit(1, 10)
#
# Cat.get_crit(1, 100)
# Cat.get_crit(1, 100)
# Cat.get_crit(1, 100)