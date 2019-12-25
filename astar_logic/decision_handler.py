from astar_logic.maze import Maze
from astar_logic.components import Node, PriorityQueue
from tools.vector import Vector


class DecisionHandler:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.visited_cells = [[float("inf") for y in range(self.maze.height)] for x in range(self.maze.width)]
        self.queue = PriorityQueue(
            [Node(maze.player_position, None, 0, self.maze.goal_position.distance_to(maze.player_position))]
        )
        self.found = False

    def update(self):
        if self.queue.has_items() and not self.found:
            current = self.queue.pop()
            if current.position.equal_to(self.maze.goal_position):
                self.show_optimal_path(current)
                self.found = True

            x, y = current.position.get_values()
            cost = current.cost + 1

            for cell in self.maze.get_valid_surrounding_cells(x, y):
                if cost < self.visited_cells[cell.x][cell.y]:
                    new_node = Node(cell, current, cost, self.maze.goal_position.distance_to(cell))
                    self.queue.insert(new_node)
                    self.visited_cells[cell.x][cell.y] = cost
                    self.maze.set_player_position(current.position)

    def show_optimal_path(self, node):
        visited = []
        while node.previous:
            visited.append(node.previous)
            node = node.previous

        for cell in visited:
            self.maze.set_maze_cell_value(cell.position, "OPTIMAL")

        print(f"Path reached in {len(visited)} steps")
