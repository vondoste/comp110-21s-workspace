"""Just fibbing around."""


def f(x: int) -> int:
    if x >= 2:
        a: int = f(x - 2)
        return a + f(x - 1)
    else:
        return x


print(f(3))