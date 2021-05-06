"""To recurse or not to recurse."""


def add(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return add(x, y - 1) + 1


def sub(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return sub(x, y - 1) - 1


def mul(x: int, y: int) -> int:
    if y == 0:
        return 0
    else:
        return mul(x, y-1) + x


def pow(x: int, y: int) -> int:
    if y == 0:
        return 1
    else:
        return pow(x, y-1) * x

def fac(x:int) -> int:
    if x == 0:
        return 1
    else:
        return fac(x-1) * x


def fib(x:int) -> int:
    if x >= 2:
        return fib(x - 2) + fib(x - 1)
    else:
        return x