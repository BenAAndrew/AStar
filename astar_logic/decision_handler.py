from astar_logic.maze import Maze
from astar_logic.components import Node, PriorityQueue, manhattan_distance


class DecisionHandler:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.queue = PriorityQueue([Node(maze.player_position, None, 0, self.distance_to_goal(maze.player_position))])
        self.found = False

    def update(self):
        if self.queue.has_items() and not self.found:
            current = self.queue.pop()
            print(current)
            if current.position == self.maze.goal_position:
                self.get_path(current)
                self.found = True

            x, y = current.position

            for cell in self.maze.get_valid_surrounding_cells(x, y):
                cost = current.cost + 1
                new_node = Node(cell, current, cost, self.distance_to_goal(cell))
                self.queue.insert(new_node)

            self.maze.set_player_position(current.position)

    def distance_to_goal(self, position):
        return manhattan_distance(self.maze.goal_position, position)

    def get_path(self, node):
        print("DONE")
        previous = []
        while node.previous:
            previous.append(node.previous)
            node = node.previous

        for p in previous:
            print(p)
