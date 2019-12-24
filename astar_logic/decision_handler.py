from astar_logic.maze import Maze
from astar_logic.components import Node, PriorityQueue
from tools.tools import manhattan_distance


class DecisionHandler:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.queue = PriorityQueue([Node(maze.player_position, None, 0, self.distance_to_goal(maze.player_position))])
        self.found = False

    def update(self):
        if self.queue.has_items() and not self.found:
            current = self.queue.pop()
            if current.position == self.maze.goal_position:
                self.show_optimal_path(current)
                self.found = True

            x, y = current.position

            for cell in self.maze.get_valid_surrounding_cells(x, y):
                cost = current.cost + 1
                new_node = Node(cell, current, cost, self.distance_to_goal(cell))
                self.queue.insert(new_node)

            self.maze.set_player_position(current.position)

    def distance_to_goal(self, position):
        return manhattan_distance(self.maze.goal_position, position)

    def show_optimal_path(self, node):
        visited = []
        while node.previous:
            visited.append(node.previous)
            node = node.previous

        for cell in visited:
            x, y = cell.position
            self.maze.set_maze_cell_value(x, y, "OPTIMAL")

        print(f"Path reached in {len(visited)} steps")
