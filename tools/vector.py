class Vector:
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
         return int(abs(self.x - vector.x) + abs(self.y - vector.y))
