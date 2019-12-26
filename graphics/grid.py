from pygame.draw import rect
from graphics.window import Window
from tools.vector import Vector
from tools.load_arguments import get_config_value

# Different cell types to represent what the cell is in the values array
# Each name also corresponds to a colour in config
CELL_VALUES = {"EMPTY": 0, "WALL": 1, "PLAYER": 2, "GOAL": 3, "VISITED": 4, "OPTIMAL": 5, "CURRENT_PATH": 6}


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
        self.colour = get_config_value("Colours", "EMPTY")
        self.value = CELL_VALUES["EMPTY"]

    def is_wall(self):
        return self.value == CELL_VALUES["WALL"]

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
            self.set_cell(cell, "WALL")
        self.set_cell(player, "PLAYER")
        self.set_cell(goal, "GOAL")

    def set_cell(self, position: Vector, value: str):
        """
        Sets a given cell to a new state.
        Updates the cell colour and value.
        
        Arguments:
            position {Vector} -- Cell position
            value {str} -- String name of value to set
        """
        x, y = position.get_values()
        self.cells[x][y].colour = get_config_value("Colours", value)
        self.cells[x][y].value = CELL_VALUES[value]

    def draw(self, window: Window):
        """
        Iterates over cells and draws each
        
        Arguments:
            window {Window} -- Window to draw to
        """
        for row in self.cells:
            for cell in row:
                cell.draw(window)
