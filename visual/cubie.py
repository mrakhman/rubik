from face import *
from sticker import Sticker
from vector import Vector


class Cubie:
    def __init__(self, pos):
        self.initial_position = pos
        self.transformations = PMatrix3D()
        self.transformations.translate(
            self.initial_position.x, self.initial_position.y, self.initial_position.z
        )

        self.stickers = [
            Sticker(
                f.initial_color
                if self._is_face_visible(self.initial_position, f.vector)
                else color(0),
                f.vector.copy().div(2),
            )
            for f in faces.values()
        ]

    @staticmethod
    def _is_face_visible(p, face):
        return p * face > 0

    def show(self, pg):
        pg.pushMatrix()
        pg.applyMatrix(self.transformations)
        for sticker in self.stickers:
            sticker.show(pg)
        pg.popMatrix()

    @property
    def position(self):
        return Vector(
            self.transformations.m03, self.transformations.m13, self.transformations.m23
        )

    def rotate(self, center, angle):
        t = PMatrix3D()

        t.translate(center.x, center.y, center.z)
        t.rotateX(angle.x)
        t.rotateY(angle.y)
        t.rotateZ(angle.z)

        reverse = -1 * center.copy()
        t.translate(reverse.x, reverse.y, reverse.z)
        self.transformations.preApply(t)


__all__ = ["Cubie"]
