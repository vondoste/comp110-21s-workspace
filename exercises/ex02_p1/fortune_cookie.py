"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730366999"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())  # Should print the string returned by fortune_cookie.
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:  # Define fortune_cookie function.
    """Generates one of 5 fortunes randomly."""
    fortune: str = "What do you want for nothing, rubber biscuit?"  # Initialize variable to hold fortune.
    msg: int = randint(1, 5)  # Declare msg as integer, and initialize it with random number from 1 to 5.

    # The following set of if statements will set fortune to be a message depending on what value msg has.
    if msg < 2:  # detects msg == 1
        fortune = "Knowing something, and thinking you know both feel the same until you are proven wrong."

    else:
        if msg < 3:  # detects msg == 2
            fortune = "'Should be' and 'Is be' ain't necessarily the same thing."

        else:
            if msg < 4:  # detects msg == 3
                fortune = "If you don't know why you are doing something, maybe you shouldn't be doing it."

            else:
                if msg < 5:  # detects msg == 4
                    fortune = "No matter where you go, there you are."

                else:   # detects if msg == 5
                    fortune = "May the bluebird of happiness leave glad tidings upon your shoulder."
    
    return fortune


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
