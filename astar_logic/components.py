from tools.vector import Vector


class Node:
    """
    Class to represent a graph node (acessible point in the maze) with a link
    to the previous node from which it was found, the cost from the start to
    reach this node (total steps) & the distance to the end.
    """

    def __init__(self, position: Vector, previous, cost: int, distance: int):
        self.position = position
        self.previous = previous
        self.cost = cost
        self.distance = distance

    def __str__(self):
        return f"{self.position[0]},{self.position[1]} (score = {self.cost+self.distance})"

    def get_score(self):
        return self.cost + self.distance

    def get_all_previous_nodes(self):
        """
        Iterates through every previous node until the start is found 
        (previous is None) and returns a list of these Nodes
        """
        node = self
        nodes = []
        while node.previous:
            node = node.previous
            nodes.append(node)
        return nodes


class PriorityQueue:
    """
    Class to store the queue of nodes to be processed
    with a priority based on the best score (lowest cost +
    distance to goal).
    """

    def __init__(self, queue: [Node]):
        self.queue = queue

    def has_items(self):
        return bool(self.queue)

    def insert(self, node: Node):
        self.queue.append(node)

    def pop(self):
        """
        Iterates over queue and gets the Node with the 
        lowest score. Will then pop this item.
        """
        max = float("inf")
        index = -1
        for i in range(len(self.queue)):
            score = self.queue[i].get_score()
            if score < max:
                max = score
                index = i
        return self.queue.pop(index)
