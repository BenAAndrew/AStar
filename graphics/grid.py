from pygame.draw import rect
from tools.vector import Vector
from tools.load_arguments import get_config_value

CELL_VALUES = {"EMPTY": 0, "WALL": 1, "PLAYER": 2, "GOAL": 3, "VISITED": 4, "OPTIMAL": 5, "CURRENT_PATH": 6}


class Cell:
    def __init__(self, position, cell_size):
        self.position = position
        self.cell_size = cell_size
        self.colour = get_config_value("Colours", "EMPTY")
        self.value = CELL_VALUES["EMPTY"]

    def is_wall(self):
        return self.value == CELL_VALUES["WALL"]

    def draw(self, window):
        rect(window, self.colour, (self.position.x, self.position.y, self.cell_size, self.cell_size))


class Grid:
    def __init__(self, window, cell_size, width, height, walls, player, goal):
        self.window = window
        self.cells = [
            [Cell(Vector((x * cell_size, y * cell_size)), cell_size) for y in range(height)] for x in range(width)
        ]
        for cell in walls:
            self.set_cell(cell, "WALL")
        self.set_cell(player, "PLAYER")
        self.set_cell(goal, "GOAL")


    def set_cell(self, position: Vector, value):
        x, y = position.get_values()
        self.cells[x][y].colour = get_config_value("Colours", value)
        self.cells[x][y].value = CELL_VALUES[value]

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.window)
