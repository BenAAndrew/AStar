from astar_logic.maze import Maze
from astar_logic.components import Node, PriorityQueue
from tools.vector import Vector


class DecisionHandler:
    """
    Class to implement A* decision making
    """

    def __init__(self, maze: Maze):
        """
        Initialises the maze as well as;
        - Visited cells (list of visited cells to avoid revisiting cells
        unless a more optimal path to that cell has been found)
        - Queue (PriorityQueue of nodes to process which has the start node
        and updates over time)
        - Continue solving (bool of whether to continue searching. This is True unless
        a path has been found or is unsolvable)
        
        Arguments:
            maze {Maze} -- Maze to solve
        """
        self.maze = maze
        self.visited_cells = [[float("inf") for y in range(self.maze.height)] for x in range(self.maze.width)]
        self.queue = PriorityQueue(
            [Node(maze.player_position, None, 0, self.maze.goal_position.distance_to(maze.player_position))]
        )
        self.continue_solving = True

    def update(self):
        """
        Update to be called at every frame of the solving process.

        Firstly checks that there are some Nodes in the queue to process.
        Otherwise the maze will not be solvable and continue_solving is set to False.

        If there are nodes it takes the highest priority one (lowest score) and firstly
        checks if this node is at the goal. If it is then the maze has been solved!

        Otherwise we check all the valid (non-wall) surrounding cells to our
        current cell and add them to the queue (if the cost to these cells are less than 
        any we have previously discovered)

        Using visited_cells helps reduce wasted time because we do not revisit cells again
        unless we know a faster route to get there. All visited_cells have an infinite value 
        at first, so will always be added to the queue the first time a cell is discovered. 
        """
        if self.queue.has_items():
            current = self.queue.pop()

            if current.position.equal_to(self.maze.goal_position):
                self.show_optimal_path(current)
                self.continue_solving = False
            else:
                cost = current.cost + 1
                for cell in self.maze.get_valid_surrounding_cells(current.position):
                    if cost < self.visited_cells[cell.x][cell.y]:
                        self.add_cell_to_queue(cell, current, cost)
        else:
            print("Maze not solvable")
            self.continue_solving = False

    def add_cell_to_queue(self, cell: Vector, current: Node, cost: int):
        """
        Creates and adds a node for a new position to the node queue.
        This is called when a new cell is found.
        
        Arguments:
            cell {Vector} -- Position of the new node/cell
            current {Node} -- The current node we are at (to be used as the previous position for the node)
            cost {int} -- The cost to get to the new node/cell
        """
        new_node = Node(cell, current, cost, self.maze.goal_position.distance_to(cell))
        self.queue.insert(new_node)
        self.visited_cells[cell.x][cell.y] = cost
        self.maze.set_player_position(current)

    def show_optimal_path(self, node: Node):
        """
        Shows the optimal path to the goal when discovered.
        
        Arguments:
            node {Node} -- The node at the goal (which can fetch all previous nodes)
        """
        visited = node.get_all_previous_nodes()
        for cell in visited:
            self.maze.grid.set_cell(cell.position, "OPTIMAL")

        print(f"Path reached in {len(visited)} steps")
