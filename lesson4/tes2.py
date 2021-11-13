from abc import ABC, abstractmethod


class Animal(ABC):
    """Абстрактный класс животных"""

    def move(self):
        print('Im moving')

    def eat(self):
        print('Im eating')

    def atack(self):
        print(f'{self.__class__.__name__} atacked some person')

    def say_hello(self):
        print('Hello')

    def func(self, name1: str, name2: str):
        print(f'{name1} something doing with {name2}')

    @abstractmethod
    def scream(self):
        pass


class Cat(Animal):

    def __init__(self, age, name):
        self.name = name
        self.age = age

    def scream(self):
        if self.age > 10:
            print(f'Meow my name is {self.name}')
        else:
            print(f'Jdjksjkdsfhkjds dfhjksdfjksh')

    def sleep(self, hours):
        print(f'I will sleep for {hours} hours')


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def scream(self):
        print(f'Gav my name is {self.name}')

    def say_hello(self):
        print('Gavgav')
        super(Dog, self).say_hello()
        print('Gav gav gav')

    def kus(self, cat: Cat):
        cat.scream()
        print(f'Dog with name {self.name} KUS cat with name {cat.name}')

    def _go_to_palka(self):
        """Это приватный метод"""
        print('I go to palke')


def eating(food_name):
    print(f'im eating {food_name}')


cat = Cat(10, 'Kitty')

cat.move()
cat.eat()
cat.say_hello()
cat.scream()
cat.atack()
cat.sleep(10)

print()

cat2 = Cat(5, 'Kate')
cat2.eat = eating
cat2.eat('bread')

print()

dog = Dog('Doggy')
dog.move()
dog.eat()
dog.say_hello()
dog.scream()
dog.atack()
dog.kus(cat)
dog.func(cat.name, cat2.name)
dog._go_to_palka()