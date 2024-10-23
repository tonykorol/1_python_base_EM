import random


class Cell:
    def __init__(self, mine: bool, around_mines: int = 0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False

    def __repr__(self):
        if self.fl_open:
            if self.mine:
                return "*"
            else:
                return str(self.around_mines)
        else:
            return "#"


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = []
        self.init()

    def init(self):
        if self.M > self.N**2:
            raise ValueError("Количество мин не должно превышать количество клеток")
        mines_indices = self.get_indices()
        for i in range(self.N):
            line = []
            for j in range(self.N):
                if (i, j) in mines_indices:
                    c = Cell(True)
                else:
                    c = Cell(False)
                line.append(c)
            self.pole.append(line)
        self.set_around_mines()

    def show(self, alls=False):
        for line in self.pole:
            for cell in line:
                if alls:
                    cell.fl_open = True
                print(cell, end='  ')
            print()

    def get_indices(self):
        indices = set()
        while len(indices) < self.M:
            i = random.randint(0, self.N-1)
            j = random.randint(0, self.N-1)
            indices.add((i, j))
        return indices

    def set_around_mines(self):
        for i, line in enumerate(self.pole):
            for j, cell in enumerate(line):
                counter = 0
                if cell.mine:
                    continue
                if j != 0 and line[j-1].mine: # по горизонтали
                    counter += 1
                if j != self.N-1 and line[j+1].mine:
                    counter += 1

                if i != 0 and self.pole[i-1][j].mine: # по вертикали
                    counter += 1
                if i != self.N-1 and self.pole[i+1][j].mine:
                    counter += 1

                if i != 0 and j != 0 and self.pole[i-1][j-1].mine: # по диагонали сверху
                    counter += 1
                if i != 0 and j != self.N-1 and self.pole[i-1][j+1].mine:
                    counter += 1
                if i != self.N-1 and j != 0 and self.pole[i+1][j-1].mine: # по диагонали снизу
                    counter += 1
                if i != self.N-1 and j != self.N-1 and self.pole[i+1][j+1].mine:
                    counter += 1

                cell.around_mines = counter

    def open(self, x, y):
        cell = self.pole[x][y]
        cell.fl_open = True
        self.show()
        if cell.mine:
            self.show(True)
            raise SystemExit("Game over")




pole_game = GamePole(10, 12)
