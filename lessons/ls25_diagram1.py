"""A class for rational numbers."""
from __future__ import annotations

class Rat:
    n: int
    d: int

    def __init__(self, n: int, d: int):
        self.n = n
        self.d = d

    def __repr__(self) -> str:
        return f"{self.n}/{self.d}"

    def __add__(self, rhs: Rat) -> Rat:
        n: int = self.n * rhs.d + rhs.n * self.d
        d: int = self.d * rhs.d
        return Rat(n, d)


x = Rat(1, 5)
y = Rat(0, 4)
z = y + x
print(z)