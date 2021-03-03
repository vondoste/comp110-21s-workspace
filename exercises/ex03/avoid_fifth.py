"""EX03 - avoid_fifth function."""

__author__: str = "730366999"


def avoid_fifth(input_string:str) -> str:
    """Remove the letter 'E' from every string."""
    output: str = ""  # Start with an empty string
    letter: str = ""  # a place to hold a letter
    i: int = 0  # Set index to 0

    while i < len(input_string):  # Use this loop to build output one letter at a time
        letter = input_string[i]  # put the indexed letter in letter.

        if "e" != letter.casefold():  # test letter to see if it's e or E
            output += letter  # If it's not an E, append it to the output string
        
        i += 1  # Increment counter

    return output  # Return our output string, no E's allowed.


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


if __name__ == "__main__":
    main()