"""A nonsensical function."""

def main() -> None:
    """This is the entry point of our nonsense"""
    my_string:str = input("Tell me something good: ")
    print(f"For {my_string}, my string_a_ling = {string_a_ling(my_string)}.")
    print(f"For {my_string}, my string_a_ling2 = {string_a_ling2(my_string)}.")

def string_a_ling(s: str) -> int:
    """Here comes the magic with an accessible index, i."""
    accumulator:int = 0
    for i in range(len(s)):
        accumulator += ord(s[i])
        print(f" {s[i]} = {ord(s[i])} ")

    accumulator = accumulator % 1000
    return accumulator


def string_a_ling2(s: str) -> int:
    """Another version, with no accessible index."""
    accumulator:int = 0
    for letter in s:
        accumulator += ord(letter)
        print(f" {letter} = {ord(letter)} ")

    accumulator = accumulator % 1000
    return accumulator


if __name__ == "__main__":
    main()

