from typing import Tuple


class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other: 'Color') -> 'Color':
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other: 'Color') -> 'Color':
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, other: 'Color') -> 'Color':
        return Color(self.r * other.r, self.g * other.g, self.b * other.b)

    def __truediv__(self, other: 'Color') -> 'Color':
        return Color(self.r / other.r, self.g / other.g, self.b / other.b)

    def __mul__(self, other: float) -> 'Color':
        return Color(self.r * other, self.g * other, self.b * other)

    def __truediv__(self, other: float) -> 'Color':
        return Color(self.r / other, self.g / other, self.b / other)

    def __eq__(self, other: 'Color') -> bool:
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __str__(self) -> str:
        return f'Color({self.r}, {self.g}, {self.b})'

    def __repr__(self) -> str:
        return f'Color({self.r}, {self.g}, {self.b})'

    def to_tuple(self) -> Tuple[float, float, float]:
        return self.r, self.g, self.b

    def to_list(self) -> Tuple[float, float, float]:
        return [self.r, self.g, self.b]
    
    def to_write(self)-> Tuple[int, int, int]:
        round_clamp = lambda value: max(0, min(255, round(value)))
        return round_clamp(self.r), round_clamp(self.g), round_clamp(self.b)