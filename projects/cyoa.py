"""PJ00 - Choose your own adventure.  Our first project
    This is my interpretation of "the shell game" (https://en.wikipedia.org/wiki/Shell_game)
    This should teach you to not play games on street corners for money.
    ** Game loop - Starts on line #44.
    ** Additional Features - lines 88, 90 and 97 change the game if the player has over $100 on the table.
                             lines 17 - 19 define an inventory of items to sell to keep playing.
                             line 64-65 ends the game if the player runs out of items to sell.
"""

__author__ = "730366999"
# use f strings, no concatenating allowed!


player: str = "nobody"  # Everybody starts out as nobody.
points: int # Keep score here.
sales_count: int = 0  # How many items have you sold
objects_to_sell: list[str] = ["pocket knife", "watch", "chain", "ring"]  # A list of four objects to pawn
prices_of_objects: list[int] = [5, 20, 30, 45]  # A list of prices for the objects in objects_to_sell, in same order.
NUMBER_OF_ITEMS: int = 4  # Must be set to the number of items in objects_to_sell & prices_of_objects.
CUP: str = "\U0001F95B"  # Unicode "glass of milk" looks like a white cup
BALL: str = "\U0001F7E2"  # Unicode "green circle" looks like a ball
WINNER: str = "\U0001F603"  # A big grin.
LOSER: str = "\U0001F622"  # Cry me a river.
MONEY: str = "\U0001F4B5"  # Show me the money.
NOT_HAPPY: str = "\U0001F620"  # A face to show you mean business.
EMBARRASSED: str = "\U0001F633"  # That's so embarrassing!
WAVE: str = "\U0001F44B"  # Waving good bye
NERVOUS: str = "\U0001F605"  # Now we're sweating.
FLAT_BROKE: int = 99  # A high value for decision that will always end the game



def main() -> None:
    """main function - Our entry point to the virtual world"""
    global points
    
    points = 0  # We start with no money on the table
    # Insert a loop somewhere in main()
    greet()
    print(f"{player} ya gotta pay if ya wanna play.")
    ante_up()  # Gotta put money on the table to move forward.
    decision: int = 0  # Flag that this hasn't been run, yet.

    while decision < 3:  # Game Loop 
        # print(f"Previous value of decision: {decision}")  # Debug statement.
        # print(f"Value of sales_count {sales_count}")  # Debug Statement.
        print(f"Well { player }, you got ${points} whatcha want to do? ")
        decision = int(input("1=play / 2=sell something / 3 or more = take a hike."))  # Choose your adventure!
        if decision == 0:
        
            # procedure call (put your pocket money on the table, or sell an item to get money
            ante_up()
            # textual interaction, use players name, ask for more input, update players score.

        if decision == 1:
            if points > 0:
                points = play_game(points)  # points = func(points) -> returns points after doing something to them.
            # call a function that takes an integer and returns an integer.  Use players name.
            else:
                print(f"{NOT_HAPPY} This ain't no bank, we don't give credit")

        if decision == 2:
            points = sell_something(points)
            if sales_count > NUMBER_OF_ITEMS:  # Determine if our pigeon has been plucked clean
                decision = FLAT_BROKE  # This should force the end of the game, since this mark is broke

    print(f"{WAVE} Alright { player }, we'll catch you next time.")
    print(f"You're walking away with ${ points }!")

    return


def greet() -> None:
    """Say hello, get the players name."""
    global player

    print(f"{WINNER} Step right up, try your luck, every game has a winner!")  # Decide on snazzy greeting    
    player = str(input("Hey Sport, what's your name?")) # Lookup the details of how to do this




def play_game(points: int) -> int:
    """ball finding begins here"""
    from random import randint
    choice: int = 0
    ball: int = randint(1,3)
    cheat: bool = points > 100 # risk mitigation strategy, cheat if thay have won more than $100
    # do something to points
    if cheat:
        print(f"{NERVOUS} Now we're playin' for BIG MONEY!")

    print("I have hidden the ball under one of these three cups.")
    print(f"{CUP} {CUP} {CUP}")
    choice = int(input("Double or nothing, which cup is the ball under (1,2, or 3)?"))

    if cheat:  # We can't afford to lose this much, so cheat
        if ball == choice:  # Detect a win and make it a lose (the dealer has fast hands!)
            # make sure they lose
            if choice == 3:
                ball = 2
            if choice == 2:
                ball = 1
            if choice == 1:
                ball = 3

    if ball < 3:  # Display which of the 3 cups has the ball
        if ball < 2:
            print(f"{BALL} {CUP} {CUP}")
        else:
            print(f"{CUP} {BALL} {CUP}")
    else:
        print(f"{CUP} {CUP} {BALL} ")

    if choice == ball:
        print(f"{WINNER} We have a Winner!  Way to double your money.")
        points = points * 2
    else:
        print(f"{LOSER} Hey, better luck next time.")
        points = 0

    return points


def ante_up() -> None:
    """How much money you got?"""
    global points
    print(f"{MONEY} It's time to put your money on the table.")
    while points < 1:
        points = int(input("How many dollars you got? We don't mess with change."))


def sell_something(points:int) -> int:
    """What has it got in it's pocketses?"""
    global sales_count
    response: str = ""

    if sales_count > NUMBER_OF_ITEMS - 1:  # make sure you don't index past the end of the lists in the next line.
        print(f"{EMBARRASSED} Pockets on empty cuz?  Come back when you got something to play with.")
        sales_count += 1  # This should trigger the FLAT_BROKE contingency.
        return points
    print(f"Hey { player }, that's a nice {objects_to_sell[sales_count]}, want to sell it?") 
    response = str(input(f" I'll give you ${prices_of_objects[sales_count]} for it (y/n)"))
    if response.casefold() == "y":
        points = points + prices_of_objects[sales_count]
        sales_count += 1

    return points


if __name__ == "__main__":
    main()