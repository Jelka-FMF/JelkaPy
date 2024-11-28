from .types import Position
from .util import distance

class Sphere:
    def __init__(self, center : Position,radius : float):
        self.center = center
        self.radius = radius
    

    def is_inside(self, pt: Position) -> bool:
        return distance(self.center, pt) <= self.radius