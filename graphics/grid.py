from pygame.draw import rect
from tools.vector import Vector


class Cell:
    def __init__(self, position, cell_size, colour):
        self.position = position
        self.cell_size = cell_size
        self.colour = colour

    def draw(self, window):
        rect(window, self.colour, (self.position.x, self.position.y, self.cell_size, self.cell_size))


class Grid:
    def __init__(self, window, cell_size, colour, width, height):
        self.window = window
        self.cells = [
            [Cell(Vector((x * cell_size, y * cell_size)), cell_size, colour) for y in range(height)] for x in range(width)
        ]

    def set_cell_colour(self, x, y, colour):
        self.cells[x][y].colour = colour

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.window)
