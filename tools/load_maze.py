import os
from enum import Enum

from tools.vector import Vector
from tools.load_arguments import get_value
from astar_logic.maze import Maze


class MazeCharacter(Enum):
    WALL = "x"
    START = "s"
    END = "e"


def get_size(lines: [str]):
    """
    Get width and height of the maze from its
    text file definition.
    
    Arguments:
        lines {[str]} -- array of lines of the file
    
    Returns:
        {int}, {int} -- width and height of the maze
    """
    height = len(lines)
    width = len(lines[0])
    for line in lines:
        assert len(line) == width, "Maze incorrectly defined (width must be consistent for all rows)"
    return width, height


def load_cells(lines: [str]):
    """
    Iterates over maze defintion to get walls
    
    Arguments:
        lines {[str]} -- list of maze lines
    
    Returns:
        {[Vector]} -- list of vector positions of walls
    """
    walls = []
    start = None
    end = None
    key_characters = [character.value for character in MazeCharacter]

    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(0, len(line)):
            char = line[x]
            if char in key_characters:
                position = Vector((x, y))
                if char == MazeCharacter.WALL.value:
                    walls.append(position)
                elif char == MazeCharacter.START.value:
                    start = position
                elif char == MazeCharacter.END.value:
                    end = position

    return walls, start, end


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

        width, height = get_size(lines)
        walls, start, end = load_cells(lines)
        cell_size = int(get_value("Visual", "Size") / max(width, height))

        return Maze(cell_size, width, height, walls, start, end), width, height, cell_size
