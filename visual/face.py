from color import Color
from vector import Vector


class Face:
    def __init__(self, name, vector, col):
        self.name = name
        self.vector = vector
        self.initial_color = col


faces = {
    "UP": Face("UP", Vector(0, -1, 0), Color.WHITE),
    "DOWN": Face("DOWN", Vector(0, 1, 0), Color.YELLOW),
    "LEFT": Face("LEFT", Vector(1, 0, 0), Color.RED),
    "RIGHT": Face("RIGHT", Vector(-1, 0, 0), Color.ORANGE),
    "FRONT": Face("FRONT", Vector(0, 0, -1), Color.BLUE),
    "BACK": Face("BACK", Vector(0, 0, 1), Color.GREEN),
}

__all__ = ["Face", "faces"]
