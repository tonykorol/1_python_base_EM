import random


class Cell:
    def __init__(self, mine: bool, around_mines: int = 0) -> None:
        self._around_mines = around_mines
        self._mine = mine
        self._fl_open: bool = False

    @property
    def around_mines(self) -> int:
        return self._around_mines

    @around_mines.setter
    def around_mines(self, around_mines: int) -> None:
        self._around_mines = around_mines

    @property
    def mine(self) -> bool:
        return self._mine

    @mine.setter
    def mine(self, mine: bool) -> None:
        self._mine = mine

    @property
    def fl_open(self) -> bool:
        return self._fl_open

    @fl_open.setter
    def fl_open(self, fl_open: bool) -> None:
        self._fl_open = fl_open

    def __repr__(self) -> str:
        if self._fl_open:
            return "*" if self._mine else str(self._around_mines)
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
        self.set_mines()

    def init_pole(self) -> list:
        empty_pole = []
        for i in range(self.N):
            empty_pole.append([Cell(False) for j in range(self.N)])
        return empty_pole

    def set_mines(self) -> None:
        mines_indices = self.get_indices()
        for l, c in mines_indices:
            self.pole[l][c].mine = True
            self.set_around_mines(l, c) # 1 1

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
    pole = GamePole(5, 10)
    pole.show(True)
