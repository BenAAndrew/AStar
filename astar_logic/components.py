class Node:
    def __init__(self, position, previous, cost, distance):
        self.position = position
        self.previous = previous
        self.cost = cost
        self.distance = distance

    def __str__(self):
        return f"{self.position[0]},{self.position[1]} (score = {self.cost+self.distance})"

    def get_score(self):
        return self.cost + self.distance

    def get_all_previous_nodes(self):
        node = self
        nodes = []
        while node.previous:
            node = node.previous
            nodes.append(node)
        return nodes


class PriorityQueue:
    def __init__(self, queue: [Node]):
        self.queue = queue

    def has_items(self):
        return bool(self.queue)

    def insert(self, node: Node):
        self.queue.append(node)

    def pop(self):
        max = float("inf")
        index = -1
        for i in range(len(self.queue)):
            score = self.queue[i].get_score()
            if score < max:
                max = score
                index = i
        item = self.queue[index]
        del self.queue[index]
        return item
