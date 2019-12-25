from graphics.grid import Grid
from tools.load_arguments import get_config_value
from tools.vector import Vector

CELL_VALUES = {"EMPTY": 0, "WALL": 1, "PLAYER": 2, "GOAL": 3, "VISITED": 4, "OPTIMAL": 5}


class Maze:
    def __init__(self, window, cell_size, width, height, wall_cells, player_position, goal_position):
        self.width = width
        self.height = height
        self.grid = Grid(window, cell_size, get_config_value("Colours", "EMPTY"), width, height)
        self.values = [[CELL_VALUES["EMPTY"] for y in range(height)] for x in range(width)]

        for cell in wall_cells:
            self.set_maze_cell_value(cell, "WALL")

        self.set_maze_cell_value(player_position, "PLAYER")
        self.player_position = player_position

        self.set_maze_cell_value(goal_position, "GOAL")
        self.goal_position = goal_position

    def set_maze_cell_value(self, position: Vector, value):
        colour = get_config_value("Colours", value)
        self.grid.set_cell_colour(position.x, position.y, colour)
        self.values[position.x][position.y] = CELL_VALUES[value]

    def within_bounds(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def is_wall(self, x, y):
        return self.values[x][y] == CELL_VALUES["WALL"]

    def get_valid_surrounding_cells(self, x, y):
        positions = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        surrounding_cells = []
        for position in positions:
            x, y = position
            if self.within_bounds(x, y) and not self.is_wall(x, y):
                surrounding_cells.append(Vector(position))
        return surrounding_cells

    def set_player_position(self, position):
        # Set old position to empty
        self.set_maze_cell_value(self.player_position, "VISITED")
        # Set new position
        self.player_position = position
        self.set_maze_cell_value(self.player_position, "PLAYER")
