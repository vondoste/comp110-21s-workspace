def main() -> None:
    n: int = 19
    x: int = fool(n+2)
    y: int = fool(52) + 2
    z: int = april(n - 18)
    print(april(fool(2)) + 1)
    print(x + y + z)  # Omit this line, only here to silence PyLance error because variables are unused.

def fool(n: int) -> int:
    if n % 2 == 0:
        return 0
    elif n >= 50:
        return 1
    elif n < 20:
        return 2
    else:
        return 3


def april(x: int) -> int:
    h: int = -110
    while x >= 0 or h < 0:
        h *= -1
        x -= 1
    return x + h


if __name__ == "__main__":
    main()