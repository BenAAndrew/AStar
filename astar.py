from time import sleep

from graphics.window import Window
from astar_logic.maze import Maze
from astar_logic.decision_handler import DecisionHandler
from tools.load_maze import load_maze
from tools.load_arguments import load_arguments, get_value, get_command_line_arg

load_arguments()

# Get key values
SLEEP_TIME = 1 / get_value("Visual", "Speed")
MAZE = load_maze(get_command_line_arg("f"))
WIDTH, HEIGHT = MAZE["size"].get_values()
CELL_SIZE = int(get_value("Visual", "Size") / max(WIDTH, HEIGHT))

# Initialise objects
screen = Window(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE, "A* maze solving")
decision_handler = DecisionHandler(Maze(CELL_SIZE, WIDTH, HEIGHT, MAZE["walls"], MAZE["start"], MAZE["end"]))

# Run process
while True:
    screen.update()
    decision_handler.maze.grid.draw(screen)
    if decision_handler.continue_solving:
        decision_handler.update()
    sleep(SLEEP_TIME)
