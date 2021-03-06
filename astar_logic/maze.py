from graphics.grid import Grid
from graphics.window import Window
from tools.load_arguments import get_value
from tools.vector import Vector
from astar_logic.components import Node, CellType


class Maze:
    def __init__(self, cell_size: int, width: int, height: int, walls: [Vector], player: Vector, goal: Vector):
        """
        Intialises the maze by setting all the cells to their correct values
        (i.e. WALL) both graphically and in code (values list)
        
        Arguments:
            cell_size {int} -- Size of each cell in pixels
            width {int} -- Maze width in cells
            height {int} -- Maze height in cells
            walls {[Vector]} --  list of Vectors with coordinates for each wall
            player {Vector} -- Vector position of the player
            goal {Vector} -- Vector position of the goals
        """
        self.width = width
        self.height = height
        self.grid = Grid(cell_size, width, height, walls, player, goal)
        self.player_position = player
        self.player_path = []
        self.goal_position = goal

    def within_bounds(self, x: int, y: int):
        """
        Checks a given x & y position is within the bounds of the maze
        
        Arguments:
            x {int} -- x coordinate
            y {int} -- y coordinate
        
        Returns:
            {bool} -- Coordinates are within bounds
        """
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def get_valid_surrounding_cells(self, position: Vector):
        """
        Find all cells surrounding a given position which are valid.
        A cell is deemed valid if within the bounds of the maze and not a wall.
        
        Arguments:
            position {Vector} -- Position to find surrounding cells for
        
        Returns:
            {[Vector]} -- List of valid surrounding positions
        """
        x, y = position.get_values()
        positions = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        surrounding_cells = []
        for position in positions:
            x, y = position
            if self.within_bounds(x, y) and not self.grid.cells[x][y].is_wall():
                surrounding_cells.append(Vector(position))
        return surrounding_cells

    def set_player_position(self, node: Node):
        """
        Sets a new player position. 
        Firstly sets the current position & path to VISITED.
        Then sets the new player position & current path
        
        Arguments:
            node {Node} -- Player position node
        """
        # Set old position to empty
        self.grid.set_cell(self.player_position, CellType.VISITED)
        # Reset old path
        for cell in self.player_path:
            self.grid.set_cell(cell, CellType.VISITED)

        # Set new position
        self.player_position = node.position
        self.grid.set_cell(self.player_position, CellType.PLAYER)
        # Set current path
        self.player_path = [cell.position for cell in node.get_all_previous_nodes()]
        for cell in self.player_path:
            self.grid.set_cell(cell, CellType.CURRENT_PATH)
