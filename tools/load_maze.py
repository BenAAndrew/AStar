import os
from tools.vector import Vector
from tools.load_arguments import get_value
from astar_logic.maze import Maze

WALL_CHARACTER = "x"


def get_coordinate_from_str(line: str):
    """
    Creates a vector for a given set of coordinates
    in the string format "x,y"
    
    Arguments:
        line {str} -- Coordinates
    
    Returns:
        {Vector} -- Vector position
    """
    return Vector(tuple([int(num) for num in line.split(",")]))


def load_walls(lines: [str]):
    """
    Iterates over maze defintion to get walls
    
    Arguments:
        lines {[str]} -- list of maze lines
    
    Returns:
        {[Vector]} -- list of vector positions of walls
    """
    walls = []

    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(0, len(line)):
            if line[x] == WALL_CHARACTER:
                walls.append(Vector((x, y)))

    return walls


def load_maze(filename: str):
    """
    Loads maze definition file in the defined format
    
    Arguments:
        filename {str} -- maze filename path
    
    Returns:
        {Maze}, {int}, {int}, {int} -- Maze and dimensions
    """
    maze_file = os.path.abspath(filename)

    with open(maze_file) as f:
        lines = [line.strip() for line in f.readlines() if line != "\n"]

        size, start, end = (get_coordinate_from_str(line) for line in lines[:3])
        width, height = size.get_values()
        walls = load_walls(lines[3:])
        cell_size = int(get_value("Visual", "Size") / max(width, height))

        return Maze(cell_size, width, height, walls, start, end), width, height, cell_size
