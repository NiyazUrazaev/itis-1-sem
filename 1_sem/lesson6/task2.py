from abc import ABC, abstractmethod
import random


class Board:

    SIZE_BOARD = 8

    def __init__(self):
        self.board_map = [
            [None for j in range(self.SIZE_BOARD)]
                for i in range(self.SIZE_BOARD)
        ]

    def generate_figures(self, n):
        for i in range(n - 1):
            figure = random.choice([
                Pawn(random.randint(0,7), random.randint(0,7)),
                Rook(random.randint(0,7), random.randint(0,7)),
                Bishop(random.randint(0,7), random.randint(0,7)),
                Horse(random.randint(0,7), random.randint(0,7)),
                Queen(random.randint(0,7), random.randint(0,7))
            ])
            self.board_map[figure.x][figure.y] = figure
        king_object = King(random.randint(0,7), random.randint(0,7))
        self.board_map[king_object.x][king_object.y] = king_object

    def show_board(self):
        for i in range(self.SIZE_BOARD):
            print(*self.board_map[i], sep="\t")


class Figure(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.__class__.__name__}"

    @abstractmethod
    def attack_pozition(self):
        pass


class Pawn(Figure):

    def attack_pozition(self):
        return [
            (self.x + 1, self.y + 1),
            (self.x - 1, self.y + 1),
        ]


class Rook(Figure):

    def attack_pozition(self):
        list_ = []
        for i in range(8):
            list_.append((self.x + i, self.y))
            list_.append((self.x - i, self.y))
            list_.append((self.x, self.y + i))
            list_.append((self.x, self.y - i))
        return list_


class Bishop(Figure):

    def attack_pozition(self):
        list_ = []
        for i in range(8):
            list_.append((self.x + i, self.y + i))
            list_.append((self.x - i, self.y + i))
            list_.append((self.x + i, self.y - i))
            list_.append((self.x - i, self.y - i))
        return list_


class Horse(Figure):

    def attack_pozition(self):
        return [
            (self.x + 2, self.y + 1), (self.x + 2, self.y -1),
            (self.x - 2, self.y + 1), (self.x - 2, self.y -1),
            (self.y + 2, self.x + 1), (self.y + 2, self.x -1),
            (self.y - 2, self.x + 1), (self.y - 2, self.x -1),
        ]


class Queen(Figure):
    def attack_pozition(self):
        list_ = []
        for i in range(8):
            list_.append((self.x + i, self.y))
            list_.append((self.x - i, self.y))
            list_.append((self.x, self.y + i))
            list_.append((self.x, self.y - i))
            list_.append((self.x + i, self.y + i))
            list_.append((self.x - i, self.y + i))
            list_.append((self.x + i, self.y - i))
            list_.append((self.x - i, self.y - i))
        return list_


class King(Figure):

    def attack_pozition(self):
        return []


board = Board()
board.generate_figures(16)
board.show_board()
