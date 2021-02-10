"""Tar Heels exercise redux as a structured program."""

__author__ = "730366999"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(number: int) -> str:  # Define tar_heels function.  Takes one int, returns a str.
    """Implements the divisible by 2 and 7 magic from EX01 tar_heels.py."""
    result: str = "insert result here."  # Declare variable to hold my result

    if 0 == number % 2:  # is number evenly divisible by 2?
        if 0 == number % 7:  # yes, is number also evenly divisible by 7?
            result = "TAR HEELS"

        else:   # no, not also evenly divisible by 7
            result = "TAR"

    else:   # not evenly divisible by 2
        if 0 == number % 7:  # is number evenly divisible by 7?
            result = "HEELS"

        else:   # not evenly divisible by either 2 or 7
            result = "CAROLINA"

    return result


if __name__ == "__main__":
    main()
