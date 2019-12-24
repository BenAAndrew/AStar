import os


def get_coordinate(line):
    return tuple([int(num) for num in line.split(",")])


def load_maze(filename):
    maze_file = os.path.abspath(filename)

    with open(maze_file) as f:
        lines = f.readlines()
        values = [get_coordinate(line[:-1]) for line in lines if line != "\n"]
        return {"size": values[0], "start": values[1], "end": values[2], "walls": values[3:]}
