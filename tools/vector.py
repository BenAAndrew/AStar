class Vector:
    """
    Class to represent a position on the maze.
    Stores x & y and enables some useful tools.
    """

    def __init__(self, tuple):
        self.x = tuple[0]
        self.y = tuple[1]

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def get_values(self):
        return self.x, self.y

    def equal_to(self, vector):
        return self.x == vector.x and self.y == vector.y

    def distance_to(self, vector):
        """
        Gets the x+y distance between itself and
        another vector
        
        Arguments:
            vector {Vector} -- Vector to measure distance to
        
        Returns:
            {int} -- total distance between vectors
        """
        return int(abs(self.x - vector.x) + abs(self.y - vector.y))
