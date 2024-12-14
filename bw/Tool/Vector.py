# Base class for vector operations
class VectorBase:
    def __init__(self):
        pass

    def __str__(self):
        return f"({', '.join(str(getattr(self, attr)) for attr in self.__annotations__)})"


class Vector2(VectorBase):
    x: float = 0
    y: float = 0

    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self.x = x
        self.y = y


class Vector3(VectorBase): 
    x: float = 0
    y: float = 0
    z: float = 0

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z


# 4D vector used for matrix operations
class VecMatrix(VectorBase):
    x: float = 0
    y: float = 0
    z: float = 0
    w: float = 0

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.w = w
