def april() -> None:
    a: list[int] = [1]
    b: list[int] = a
    a = fools(b)
    print(a[0] + b[0])


def fools(a: list[int]) -> list[int]:
    b: list[int] = a
    a = [3]
    b[0] = 2
    return a


april()