from cubie import Cubie
from face import Face
from vector import Vector


class Cube:
    def __init__(self):
        self.cubies = [
            Cubie(Vector(x, y, z))
            for z in range(-1, 2)
            for y in range(-1, 2)
            for x in range(-1, 2)
            if not (x == y == z == 0)
        ]

    def show(self, pg):
        for cubie in self.cubies:
            cubie.show(pg)

    def rotate_face(self, face, clockwise=True):
        face_cubies = self.select_face_cubies(face)
        angle = face.vector.copy().setMag(HALF_PI).mult(1 if clockwise else -1)
        for cubie in face_cubies:
            cubie.rotate(face.vector, angle)

    def select_face_cubies(self, face):
        return [
            cubie for cubie in self.cubies if round(cubie.position * face.vector, 2) > 0
        ]


__all__ = ["Cube"]
