from typing import Union

from ..types import Position


class Plane:
    def __init__(
        self,
        center: Union[Position, tuple[float, float, float]],
        normal: Union[Position, tuple[float, float, float]],
    ):
        self.center = Position(*center)
        self.normal = Position(*normal)
        self.d = self.center.dot(self.normal)
