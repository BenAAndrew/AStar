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


def manhattan_distance(position_a, position_b):
    return int(abs(position_a[0] - position_b[0]) + abs(position_a[1] - position_b[1]))
