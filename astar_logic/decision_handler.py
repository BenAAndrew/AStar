from astar_logic.maze import Maze


class DecisionHandler:
    def update(self, maze: Maze):
        if maze.player_position[0] < 2:
            maze.set_player_position((maze.player_position[0] + 1, maze.player_position[1]))
        else:
            maze.set_player_position((maze.player_position[0] - 1, maze.player_position[1]))
