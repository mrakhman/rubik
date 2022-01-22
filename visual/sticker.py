class Sticker:
    def __init__(self, face_color, position):
        self.color = face_color
        self.transformations = PMatrix3D()
        self.transformations.translate(position.x, position.y, position.z)

        if position.y != 0:
            self.transformations.rotateX(HALF_PI)
        if position.x != 0:
            self.transformations.rotateY(HALF_PI)

    def show(self, pg):
        pg.pushMatrix()
        pg.applyMatrix(self.transformations)
        pg.fill(self.color)
        pg.stroke(0)
        pg.strokeWeight(0.025)
        pg.square(0, 0, 1)
        pg.popMatrix()


__all__ = ["Sticker"]
