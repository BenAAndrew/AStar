from graphics.grid import Grid
from load_config import get_value

CELL_VALUES = {"EMPTY": 0, "WALL": 1, "PLAYER": 2, "GOAL": 3}


class Maze:
    def __init__(self, window, cell_size, width, height):
        self.grid = Grid(window, cell_size, get_value("Colours", "EMPTY"), width, height)
        self.values = [[CELL_VALUES["EMPTY"] for x in range(width)] for y in range(height)]

    def set_maze_cell_value(self, x, y, value):
        colour = get_value("Colours", value)
        self.grid.set_cell_colour(x, y, colour)
        self.values[x][y] = CELL_VALUES[value]
