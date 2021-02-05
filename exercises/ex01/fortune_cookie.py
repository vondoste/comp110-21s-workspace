"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730366999"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

# Declare msg as integer, and initialize it with random number from 1 to 5
msg: int = randint(1, 5)
# print("msg = " + str(msg))  # display value of msg to verify that I display the correct message

# Print first line
print("Your fortune cookie says...")

# Select "fortune" for the second line of output
if msg < 2:  # detects msg == 1
    print("May the bluebird of happiness leave glad tidings upon your shoulder.")

else:
    if msg < 3:  # detects msg == 2
        print("'Should be' and 'Is be' ain't necessarily the same thing.")

    else:
        if msg < 4:  # detects msg == 3
            print("No matter where you go, there you are.")

        else:
            if msg < 5:  # detects msg == 4
                print("If you don't know why you are doing something, maybe you shouldn't be doing it.")

            else:   # detects if msg == 5
                print("Knowing something, and thinking you know both feel the same until you are proven wrong.")                 

# Print last line
print("Now, go spread positive vibes!")