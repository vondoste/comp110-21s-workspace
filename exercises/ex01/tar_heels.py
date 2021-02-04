"""An exercise in remainders and boolean logic."""

__author__ = "730366999"


# Begin your solution here...
# Declare number as an int, initialize it with user input value.
number: int = int(input("Enter an int: "))

if 0 == number % 2: # is number evenly divisible by 2?
    if 0 == number % 7: # yes, is number also evenly divisible by 7?
        print("TAR HEELS")

    else:   # no, not also evenly divisible by 7
        print("TAR")

else:   #not evenly divisible by 2
    if 0 == number % 7: #is number evenly divisible by 7?
        print("HEELS")

    else:   #not evenly divisible by either 2 or 7
        print("CAROLINA")