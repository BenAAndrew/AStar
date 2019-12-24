from graphics.grid import Grid
from load_config import get_value


class Maze:
    def __init__(self, window, cell_size, width, height):
        self.grid = Grid(window, cell_size, get_value("Colours", "Empty_Cell"), width, height)
        self.values = [[0 for x in range(width)] for y in range(height)]
