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
    
    def simplify(self) -> Rat:
        gcd = self.d // 2
        while gcd > 1:
            if self.n % gcd == 0 and self.d % gcd == 0:
                return Rat(self.n // gcd, self.d // gcd)
            else:
                gcd -= 1
        return self


x = Rat(6, 8)
y = Rat(1, 2)

simp_y = y.simplify()
print(simp_y)

simp_x = x.simplify()
print(simp_x)