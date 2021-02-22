"""PJ00 - Choose your own adventure.  Our first project
    include description of above and beyond options
"""

__author__ = "730366999"
# use f strings, no concatenating allowed!


player: str = "nobody"  # Everybody starts out as nobody.
points: int # Keep score here.
UNICODE_ESCAPE: str = "\U00000000"  # Unicode escape sequence (required named constant)


def main() -> None:
    """main function - Our entry point to the virtual world"""
    global points = 0  # Everybody starts with nothing. - verify that this is right!
    # Insert a loop somewhere in main()
    greet()
    decision: int = int(input("enter your choice"))  # supply details later
    if decision == 1:
        # procedure call (put your pocket money on the table, or sell an item to get money
        # What has it got in its pocketses?!?!?
        # textual interaction, use players name, ask for more input, update players score.


    if decision == 2:
        #do something else
        # call a function that takes an integer and returns an integer.  Use players name.
        points = play_game(points)  # points = func(points) -> returns points after doing something to them.
        #find the ping pong ball?  Use an element of randomness
    # print goodbye
    # print score

    return


def greet() -> None:
    """docstring"""
    print("Hello ")  # Decide on snazzy greeting
    # Step right up, try your luck, every game has a winner!
    global player = str(input("What is your name?")) # Lookup the details of how to do this


def play_game(points: int) -> int:
    """ball finding begins here"""
    # do something to points
    # 
    return points


if __name__ == "__main__":
    main()