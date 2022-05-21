from game.controller import CellType, Controller


class TestController:
    @classmethod
    def setup_class(cls):
        from kivy.logger import LOG_LEVELS, Logger

        Logger.setLevel(LOG_LEVELS["debug"])
        cls.c = Controller(rows=4, columns=4)
        cls.c.setup()

    def test_controller(self):
        assert len(self.c.board) == 16
        assert len([i for i in self.c.board if i.cell_type == CellType.SPACE]) == 1
        numbers = [i for i in self.c.board if i.cell_type == CellType.NUMBER]
        assert len(numbers) == len(self.c.board) - 1
        assert self.c.board[-1].cell_type == CellType.SPACE

    def test_make_move(self):
        self.c.make_move(len(self.c.board) - 2)
        assert self.c.board[-1].cell_type == CellType.NUMBER
        assert self.c.board[-2].cell_type == CellType.SPACE

    def test_get_neighbors(self):
        assert self.c.board[0].get_neighbor_positions() == {1, 4}
        assert self.c.board[6].get_neighbor_positions() == {5, 7, 2, 10}

    def test_game_is_over(self):
        assert not self.c.game_is_over
        self.c.board.sort(key=lambda i: i.number)
        assert self.c.game_is_over
