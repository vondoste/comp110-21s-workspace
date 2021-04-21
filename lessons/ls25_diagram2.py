"""Another Docstring."""

from __future__ import annotations
from typing import Union

class Node:
    v: int
    next: Union[Node, None]

    def __init__(self, v: int, next: Union[Node, None]):
        self.v = v
        self.next = next
    
    def __repr__(self) -> str:
        r: str = f"{self.v} -> "
        n: Union[Node, None] = self.next
        while isinstance(n, Node):
            r += f"{n.v} -> "
            n = n.next
        r += "None"
        return r


n1 = Node(1, None)
n2 = Node(2, n1)

print(n2)