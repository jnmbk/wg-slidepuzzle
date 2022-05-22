from kivy.app import App
from kivy.uix.button import Button

from .controller import CellType, Controller


class Game(App):
    def build(self):
        self.load_kv()

        self.controller = Controller()
        self.controller.setup()
        self.load_cells()

    def load_cells(self):
        for i, cell in enumerate(self.controller.board):
            button = Button(
                text=str(cell.number) if cell.cell_type == CellType.NUMBER else "",
                disabled=not cell.is_enabled,
            )
            button.cell = cell

            def make_move(button):
                self.controller.make_move(button.cell.cell_index)
                self.refresh_cells()
                if self.controller.game_is_over:
                    for button in self.root.ids.grid.children:
                        button.disabled = True
                    self.root.ids.game_over_label.opacity = 1

            button.bind(on_press=make_move)
            self.root.ids.grid.add_widget(button)

    def refresh_cells(self):
        for button, cell in zip(
            reversed(self.root.ids.grid.children), self.controller.board
        ):
            button.cell = cell
            button.text = str(cell.number if cell.cell_type == CellType.NUMBER else "")
            button.disabled = not cell.is_enabled


def main():
    Game().run()


if __name__ == "__main__":
    main()
