from pygame.draw import rect


class Cell:
    def __init__(self, x, y, cell_size, colour):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.colour = colour

    def draw(self, window):
        rect(window, self.colour, (self.x, self.y, self.cell_size, self.cell_size))


class Grid:
    def __init__(self, window, cell_size, colour, width, height):
        self.window = window
        self.cells = [
            [Cell(x * cell_size, y * cell_size, cell_size, colour) for x in range(width)] for y in range(height)
        ]

    def set_cell_colour(self, x, y, colour):
        self.cells[x][y].colour = colour

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.window)
