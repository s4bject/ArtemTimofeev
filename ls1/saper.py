from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False  # True - все клетки изначально открыты, False - закрыты


class GamePole:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.pole = [[Cell() for _ in range(n)] for _ in range(n)]
        self.init()

    def init(self):
        total_mines = 0
        while total_mines < self.m:
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)
            if not self.pole[i][j].mine:
                self.pole[i][j].mine = True
                total_mines += 1

            for x in range(max(0, i - 1), min(self.n, i + 2)):
                for y in range(max(0, j - 1), min(self.n, j + 2)):
                    self.pole[x][y].around_mines += 1

    def show(self):
        for r in self.pole:
            line = ""
            for c in r:
                if not c.fl_open:
                    line += "# "
                elif c.mine:
                    line += "* "
                else:
                    line += f"{c.around_mines} "
            print(line.strip())
        print()

    def open_cell(self, x: int, y: int):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.pole[x][y].fl_open = True