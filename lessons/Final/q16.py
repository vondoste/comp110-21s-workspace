from __future__ import annotations
from typing import Union

class Mul:
    lhs: Union[Div, Mul, int]
    rhs: Union[Div, Mul, int]

    def eval(self) -> int:
        lhs = eval(self.lhs)
        rhs = eval(self.rhs)
        return lhs * rhs

class Div:
    lhs: Union[Div, Mul, int]
    rhs: Union[Div, Mul, int]

    def eval(self) -> int:
        lhs = eval(self.lhs)
        rhs = eval(self.rhs)
        return lhs // rhs

def eval(e: Union[Div, Mul, int]) -> int:
    if isinstance(e, int):
        return e
    else:
        return e.eval()

e = Div()
e.lhs = 6
e.rhs = Mul()
e.rhs.lhs = 2
e.rhs.rhs = 3
print(e.eval())