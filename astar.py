from time import sleep

from graphics.window import Window
from graphics.grid import Grid
from load_config import get_value

SLEEP_TIME = 1 / get_value("Visual", "Speed")
GRID_SIZE = (3, 3)

# Initialise objects
cell_size = get_value("Visual", "Cell_Size")
screen = Window(GRID_SIZE[0] * cell_size, GRID_SIZE[1] * cell_size, "A* maze solving")
grid = Grid(screen.screen, cell_size, get_value("Colours", "Empty_Cell"), GRID_SIZE[0], GRID_SIZE[1])

# Run process
while True:
    screen.update(grid)
    sleep(SLEEP_TIME)
