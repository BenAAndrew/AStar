from graphics.grid import Grid
from tools.load_arguments import get_config_value
from tools.vector import Vector
from astar_logic.components import Node


class Maze:
    def __init__(self, window, cell_size, width, height, wall_cells, player_position, goal_position):
        self.width = width
        self.height = height
        self.grid = Grid(window, cell_size, width, height)

        for cell in wall_cells:
            self.grid.set_cell(cell, "WALL")

        self.grid.set_cell(player_position, "PLAYER")
        self.player_position = player_position
        self.player_path = []

        self.grid.set_cell(goal_position, "GOAL")
        self.goal_position = goal_position

    def within_bounds(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def get_valid_surrounding_cells(self, x, y):
        positions = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        surrounding_cells = []
        for position in positions:
            x, y = position
            if self.within_bounds(x, y) and not self.grid.cells[x][y].is_wall():
                surrounding_cells.append(Vector(position))
        return surrounding_cells

    def set_player_position(self, node: Node):
        # Set old position to empty
        self.grid.set_cell(self.player_position, "VISITED")
        # Reset old path
        for cell in self.player_path:
            self.grid.set_cell(cell, "VISITED")

        # Set new position
        self.player_position = node.position
        self.grid.set_cell(self.player_position, "PLAYER")
        # Set current path
        self.player_path = [cell.position for cell in node.get_all_previous_nodes()]
        for cell in self.player_path:
            self.grid.set_cell(cell, "CURRENT_PATH")
