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
    global points
    
    points = 0  # Everybody starts with nothing. 
    # Insert a loop somewhere in main()
    greet()
    decision: int = int(input(f"Hey { player }, whatcha want to do? (1=bet/2=play/3=sell/4 or more = take a hike."))  # supply details later
    if decision == 1:
        
        # procedure call (put your pocket money on the table, or sell an item to get money
        ante_up()
        # textual interaction, use players name, ask for more input, update players score.

    if decision == 2:
        
        # call a function that takes an integer and returns an integer.  Use players name.
        points = play_game(points)  # points = func(points) -> returns points after doing something to them.
        #find the ping pong ball?  Use an element of randomness

    if decision == 3:
        points = sell_something(points)
        # track how many times something is sold, and play with messages.

    print(f"Alright { player }, we'll catch you next time.")
    print(f"You're walking away with ${ points }!")

    return


def greet() -> None:
    """Say hello, get the players name."""
    global player

    print("Step right up, try your luck, every game has a winner!")  # Decide on snazzy greeting    
    player = str(input("Hey Sport, what's your name?")) # Lookup the details of how to do this




def play_game(points: int) -> int:
    """ball finding begins here"""
    from random import randint
    choice: int = 0
    ball: int = randint(1,3)
    # do something to points
    print("I have hidden the ball under one of these three cups.")
    print("  \U0001F95B \U0001F95B \U0001F95B ")
    choice = int(input("Double or nothing, which cup is the ball under (1,2, or 3)?"))
    if ball < 3:  # Display which of the 3 cups has the ball
        if ball < 2:
            print("  \U0001F7E2 \U0001F95B \U0001F95B  ")
        else:
            print("  \U0001F95B \U0001F7E2 \U0001F95B  ")
    else:
        print("  \U0001F95B \U0001F95B \U0001F7E2 ")

    if choice == ball:
        print("We have a Winner! Way to double your money.")
        points = points * 2
    else:
        print("Hey, better luck next time.")
        points = 0

    return points


def ante_up() -> None:
    """How much money you got?"""
    global points
    print(f"Alright { player }, it's time to put your money on the table.")
    points = int(input("How many dollars you got, we don't mess with small change?"))


def sell_something(points:int) -> int:
    """What has it got in it's pocketses?"""
    PRICE_OF_WATCH: int = 30  # What I'll pay a sucker for a gold watch
    response: str = ""

    response = str(input(f"Hey { player }, that's a nice watch, want to sell it?  I'll give you $30 for it (y/n)"))
    if response.casefold() == "y":
        points = points + PRICE_OF_WATCH

    return points


if __name__ == "__main__":
    main()