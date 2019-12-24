from time import sleep

from graphics.window import Window
from astar_logic.maze import Maze
from load_config import get_value

SLEEP_TIME = 1 / get_value("Visual", "Speed")
GRID_SIZE = (3, 3)

# Initialise objects
cell_size = get_value("Visual", "Cell_Size")
screen = Window(GRID_SIZE[0] * cell_size, GRID_SIZE[1] * cell_size, "A* maze solving")
maze = Maze(screen.screen, cell_size, GRID_SIZE[0], GRID_SIZE[1])
maze.set_maze_cell_value(0, 0, "WALL")
maze.set_maze_cell_value(0, 1, "PLAYER")
maze.set_maze_cell_value(2, 1, "GOAL")

# Run process
while True:
    screen.update(maze.grid)
    sleep(SLEEP_TIME)
