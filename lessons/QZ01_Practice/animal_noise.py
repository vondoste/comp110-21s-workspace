"""A program which produces some animal noises."""

def main() -> None:
    """Entrypoint of program."""
    x: int = 2
    sound: str = animal_noise(foo(x))
    print(animal_noise(x + 3))
    print(sound)


def animal_noise(x: int) -> str:
    """A silly function that returns animal noises."""
    if x < 7:
        if x < 5:
            print("the mouse goes")
            return "squeek"
        else:
            print("the cow goes")        
            return "moo"
    if x < 10:
        print("the cat goes")
        return "meow"
    return "woof"


def foo(y: int) -> int:
    """A silly function."""
    result: int = y + 1
    return y * 2


if __name__ == "__main__":
    main()