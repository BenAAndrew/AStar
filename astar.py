from time import sleep

from graphics.window import Window
from astar_logic.maze import Maze
from astar_logic.decision_handler import DecisionHandler
from tools.load_maze import load_maze
from load_config import get_value

SLEEP_TIME = 1 / get_value("Visual", "Speed")
MAZE = load_maze("mazes/maze1.txt")
WIDTH, HEIGHT = MAZE["size"].get_values()
CELL_SIZE = int(get_value("Visual", "Size") / max(WIDTH, HEIGHT))

# Initialise objects
screen = Window(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE, "A* maze solving")
decision_handler = DecisionHandler(
    Maze(screen.screen, CELL_SIZE, WIDTH, HEIGHT, MAZE["walls"], MAZE["start"], MAZE["end"])
)

# Run process
while True:
    screen.update()
    decision_handler.maze.grid.draw()
    decision_handler.update()
    sleep(SLEEP_TIME)
