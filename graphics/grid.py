from pygame.draw import rect

from astar_logic.components import CellType
from graphics.window import Window
from tools.vector import Vector
from tools.load_arguments import get_value


class Cell:
    """
    Representation of a Grid Cell. Holds the colour 
    and rendering for a single cell, as well as the 
    cells value in code (i.e. WALL)
    """

    def __init__(self, position: Vector, cell_size: int):
        self.position = position
        self.cell_size = cell_size
        # Defaults each cell to EMPTY
        self.colour = get_value("Colours", CellType.EMPTY.name)
        self.value = CellType.EMPTY

    def is_wall(self):
        return self.value == CellType.WALL

    def draw(self, window: Window):
        """
        Draws a given cell to the pygame window
        
        Arguments:
            window {Window} -- Window to draw to
        """
        rect(window.screen, self.colour, (self.position.x, self.position.y, self.cell_size, self.cell_size))


class Grid:
    """
    Represents the grid (group of cells) in the maze.
    Initialises the different key cell types (MAZE, PLAYER & GOAL)
    """

    def __init__(self, cell_size: int, width: int, height: int, walls: [Vector], player: Vector, goal: Vector):
        """
        Intialises all the cells of the grid and sets the WALL, PLAYER & GOAL cells
        
        Arguments:
            cell_size {int} -- size of cell in pixels
            width {int} -- width of maze in cells
            height {int} -- height of maze in cells
            walls {[Vector]} -- list of wall positions
            player {Vector} -- player starting position
            goal {Vector} -- goal position
        """
        self.cells = [
            [Cell(Vector((x * cell_size, y * cell_size)), cell_size) for y in range(height)] for x in range(width)
        ]
        for cell in walls:
            self.set_cell(cell, CellType.WALL)
        self.set_cell(player, CellType.PLAYER)
        self.set_cell(goal, CellType.GOAL)

    def set_cell(self, position: Vector, value: CellType):
        """
        Sets a given cell to a new state.
        Updates the cell colour and value.
        
        Arguments:
            position {Vector} -- Cell position
            value {CellType} -- CellType to set
        """
        x, y = position.get_values()
        self.cells[x][y].colour = get_value("Colours", value.name)
        self.cells[x][y].value = value

    def draw(self, window: Window):
        """
        Iterates over cells and draws each
        
        Arguments:
            window {Window} -- Window to draw to
        """
        for row in self.cells:
            for cell in row:
                cell.draw(window)
