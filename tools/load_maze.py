import os
from tools.vector import Vector


def get_coordinate_from_str(line):
    return Vector(tuple([int(num) for num in line.split(",")]))


def load_maze(filename):
    maze_file = os.path.abspath(filename)

    with open(maze_file) as f:
        lines = f.readlines()
        values = [get_coordinate_from_str(line[:-1]) for line in lines if line != "\n"]
        return {"size": values[0], "start": values[1], "end": values[2], "walls": values[3:]}
