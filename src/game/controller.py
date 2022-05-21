import random
from dataclasses import dataclass
from enum import Enum

from kivy.logger import Logger


class CellType(Enum):
    NUMBER = "number"
    SPACE = "space"


class Controller:
    def __init__(self, rows: int = 4, columns: int = 4) -> None:
        self.board: list[Cell] = []
        self.rows = rows
        self.columns = columns
        self.space_cell_index = rows * columns - 1

    def setup(self):
        for i in range(self.rows * self.columns - 1):
            self.board.append(Cell(self, i + 1))
        random.shuffle(self.board)
        self.board.append(Cell(self, -1, cell_type=CellType.SPACE))

        self.update_enabled_status()
        Logger.debug(f"App: Board: {[i.number for i in self.board]}")

    def make_move(self, index: int):
        Logger.debug(f"App: Making move on {self.board[index].number}")
        # swap given number cell with the space cell
        assert self.board[index].is_enabled
        space_cell_is_before = self.space_cell_index < index
        space_cell = self.board.pop(self.space_cell_index)
        number_cell = self.board.pop(index - 1 if space_cell_is_before else index)
        self.board.insert(
            self.space_cell_index
            if space_cell_is_before
            else self.space_cell_index - 1,
            number_cell,
        )
        self.board.insert(index, space_cell)
        self.space_cell_index = index
        self.update_enabled_status()

        Logger.debug(f"App: Done move on {index}")
        Logger.debug(f"App: Board: {[i.number for i in self.board]}")

    def update_enabled_status(self):
        space_cell = self.board[self.space_cell_index]
        space_neighbors = space_cell.get_neighbor_positions()

        for i, cell in enumerate(self.board):
            cell.is_enabled = i in space_neighbors

    @property
    def game_is_over(self):
        return [i.number for i in self.board if i.cell_type == CellType.NUMBER] == list(
            range(1, len(self.board))
        )


@dataclass
class Cell:
    controller: Controller
    number: int
    cell_type: CellType = CellType.NUMBER
    _is_enabled: bool = False

    @property
    def cell_index(self) -> int:
        return self.controller.board.index(self)

    @property
    def position(self) -> tuple[int, int]:
        index = self.cell_index
        return index // self.controller.rows, index % self.controller.columns

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value) -> None:
        if self._is_enabled == value:
            return
        Logger.debug(f"App: {'En' if value else 'Dis'}abling cell {self.number}")
        self._is_enabled = value

    def get_neighbor_positions(self) -> set[int]:
        row, column = self.position
        neighbor_positions = set()
        if row > 0:
            neighbor_positions.add(self.cell_index - self.controller.columns)
        if row < self.controller.rows:
            neighbor_positions.add(self.cell_index + self.controller.columns)
        if column > 0:
            neighbor_positions.add(self.cell_index - 1)
        if column < self.controller.columns:
            neighbor_positions.add(self.cell_index + 1)
        return neighbor_positions
