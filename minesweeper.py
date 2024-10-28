import random


class Cell:
    def __init__(self, mine: bool = False, around_mines: int = 0) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.mine if self.mine else self.around_mines})"

    def __str__(self) -> str:
        if self.fl_open:
            return "*" if self.mine else str(self.around_mines)
        else:
            return "#"

class GamePole:
    AROUND_CELLS_INDEX_DELTA = ((-1, -1), (-1, 0),
                                (-1, 1), (0, -1),
                                (0, 1), (1, -1),
                                (1, 0), (1, 1))

    def __init__(self, N: int, M: int) -> None | Exception:
        if N**2 < M:
            raise ValueError("Количество мин больше количества клеток")
        self.N = N
        self.M = M
        self.pole = self.init_pole()
        self.generate_mines()

    def init_pole(self) -> list:
        empty_pole = []
        for _ in range(self.N):
            empty_pole.append([Cell() for _ in range(self.N)])
        return empty_pole

    def generate_mines(self):
        mines_indices = self.get_indices()
        for l, c in mines_indices:
            self.set_mine(l, c)

    def set_mine(self, l, c) -> None:
        self.pole[l][c].mine = True
        self.set_around_mines(l, c)

    def set_around_mines(self, l: int, c: int) -> None:
        for dl, dc in self.AROUND_CELLS_INDEX_DELTA:
            nl, nc = l + dl, c + dc
            if 0 <= nl < self.N and 0 <= nc < self.N:
                self.pole[nl][nc].around_mines += 1

    def get_indices(self) -> set:
        indices = set()
        while len(indices) < self.M:
            i = random.randint(0, self.N-1)
            j = random.randint(0, self.N-1)
            indices.add((i, j))
        return indices

    def show(self, alls=False) -> None:
        for line in self.pole:
            for cell in line:
                if alls:
                    cell.fl_open = True
                print(cell, end='  ')
            print()


if __name__ == "__main__":
    pole = GamePole(5, 5)
    pole.show(True)
