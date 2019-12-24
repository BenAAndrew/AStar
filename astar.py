from time import sleep

from graphics.window import Window
from astar_logic.maze import Maze
from astar_logic.decision_handler import DecisionHandler
from tools.load_maze import load_maze
from load_config import get_value

SLEEP_TIME = 1 / get_value("Visual", "Speed")
maze = load_maze("mazes/maze1.txt")
width, height = maze["size"].get_values()

# Initialise objects
cell_size = get_value("Visual", "Cell_Size")
screen = Window(width * cell_size, height * cell_size, "A* maze solving")
decision_handler = DecisionHandler(
    Maze(screen.screen, cell_size, width, height, maze["walls"], maze["start"], maze["end"])
)

# Run process
while True:
    screen.update()
    decision_handler.maze.grid.draw()
    decision_handler.update()
    sleep(SLEEP_TIME)
