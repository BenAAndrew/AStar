from time import sleep

from graphics.window import Window
from astar_logic.decision_handler import DecisionHandler
from tools.load_maze import load_maze
from tools.load_arguments import load_arguments, get_value, get_command_line_arg

load_arguments()

# Get key values
SLEEP_TIME = 1 / get_value("Visual", "Speed")
MAZE, WIDTH, HEIGHT, CELL_SIZE = load_maze(get_command_line_arg("f"))

# Initialise objects
screen = Window(WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE, "A* maze solving")
decision_handler = DecisionHandler(MAZE)

# Run process
while True:
    """
    Main running process.
    Updates the screen & renders the grid.
    If the maze is still being solved it also 
    updates decision_handler to execute the 
    next step in the solve.
    """
    screen.update()
    decision_handler.maze.grid.draw(screen)
    if decision_handler.continue_solving:
        decision_handler.update()
    sleep(SLEEP_TIME)
