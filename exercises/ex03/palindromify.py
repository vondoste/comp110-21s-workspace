"""EX03 - palindromify function."""

__author__: str = "730366999"


def palindromify(word: str, even: bool) -> str:
    """Will make a palindrome from your input string, specify if it will be even or odd in length."""
    i: int = len(word) - 1  # set loop index last character in word.

    if not even:  # if odd, subtract 1 from i to not duplicate the last letter.
        i -= 1

    while not (i < 0):  # Start at last letter in original string, work your way to first letter.
        word += word[i]   # append the [i]th letter to word, this builds second half of palindrome.
        i -= 1  # reduce i by one, select the next letter 

    return word


def main() -> None:
    """Entrypoint of the program."""  # Just a bunch of test cases for palindromify.
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


if __name__ == "__main__":
    main()