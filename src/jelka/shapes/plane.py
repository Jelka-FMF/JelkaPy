from ..types import Position


class Plane:
    def __init__(
        self,
        center: "Position | tuple[float, float, float]",
        normal: "Position | tuple[float, float, float]",
    ):
        self.center = Position(*center)
        self.normal = Position(*center)
        self.d = normal[0] * center[0] + normal[1] * center[1] + normal[2] * center[2]
