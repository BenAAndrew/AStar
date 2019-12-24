from graphics.grid import Grid
from load_config import get_value

CELL_VALUES = {"EMPTY": 0, "WALL": 1, "PLAYER": 2, "GOAL": 3}


class Maze:
    def __init__(self, window, cell_size, width, height, wall_cells, player_position, goal_position):
        self.grid = Grid(window, cell_size, get_value("Colours", "EMPTY"), width, height)
        self.values = [[CELL_VALUES["EMPTY"] for y in range(height)] for x in range(width)]

        for cell in wall_cells:
            self.set_maze_cell_value(cell[0], cell[1], "WALL")

        self.set_maze_cell_value(player_position[0], player_position[1], "PLAYER")
        self.player_position = player_position

        self.set_maze_cell_value(goal_position[0], goal_position[1], "GOAL")
        self.goal_position = goal_position

    def set_maze_cell_value(self, x, y, value):
        colour = get_value("Colours", value)
        self.grid.set_cell_colour(x, y, colour)
        self.values[x][y] = CELL_VALUES[value]

    def set_player_position(self, position):
        # Set old position to empty
        self.set_maze_cell_value(self.player_position[0], self.player_position[1], "EMPTY")
        # Set new position
        self.player_position = position
        self.set_maze_cell_value(self.player_position[0], self.player_position[1], "PLAYER")
