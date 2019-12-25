import os
from tools.vector import Vector

WALL_CHARACTER = "x"


def get_coordinate_from_str(line):
    return Vector(tuple([int(num) for num in line.split(",")]))


def load_walls(lines):
    walls = []

    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(0, len(line)):
            if line[x] == WALL_CHARACTER:
                walls.append(Vector((x, y)))

    return walls


def load_maze(filename):
    maze_file = os.path.abspath(filename)

    with open(maze_file) as f:
        lines = [line.strip() for line in f.readlines() if line != "\n"]
        size, start, end = (get_coordinate_from_str(line) for line in lines[:3])
        return {"size": size, "start": start, "end": end, "walls": load_walls(lines[3:])}
