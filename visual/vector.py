class Vector(PVector):
    def __mul__(self, other):
        if isinstance(other, PVector):
            return self.x * other.x + self.y * other.y + self.z * other.z

        return super(Vector, self).__mul__(other)

    def __rmul__(self, other):
        return self * other


__all__ = ["Vector"]
