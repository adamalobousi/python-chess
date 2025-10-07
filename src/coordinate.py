class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}:{self.y}"
    
    def __eq__(self, value: object):
        return isinstance(value, Coordinate) and self.x == value.x and self.y == value.y
    
class Move:
    def __init__(self, start, destination):
        self.start = start
        self.destination = destination
    
    def __str__(self) -> str:
        return str(self.start) + "->" + str(self.destination)
    
    def __eq__(self, value):
        return isinstance(value, Move) and self.start == value.start and self.destination == value.destination