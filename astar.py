from time import sleep

from graphics.window import Window
from astar_logic.maze import Maze
from astar_logic.decision_handler import DecisionHandler
from load_config import get_value

SLEEP_TIME = 1 / get_value("Visual", "Speed")
GRID_SIZE = (5, 5)

# Initialise objects
cell_size = get_value("Visual", "Cell_Size")
screen = Window(GRID_SIZE[0] * cell_size, GRID_SIZE[1] * cell_size, "A* maze solving")
decision_handler = DecisionHandler(
    Maze(screen.screen, cell_size, GRID_SIZE[0], GRID_SIZE[1], [(0, 0), (2, 2), (0, 2)], (0, 1), (3, 3))
)

# Run process
while True:
    screen.update(decision_handler.maze.grid)
    decision_handler.update()
    sleep(SLEEP_TIME)
