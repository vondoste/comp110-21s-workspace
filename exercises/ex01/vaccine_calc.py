"""A vaccination calculator."""

__author__ = "730366999"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
# Declare and initialize our variables
population: int = 2 * int(input("Population: "))  # keep number of doses needed (2 doses per person).
doses_admin: int = int(input("Doses Administered: "))    # keep doses administered here
doses_per_day: int = int(input("Doses per day: "))   # keep doses per day here
target_percent: int = int(input("Target percent vaccinated: "))  # keep target percentage here
target_doses: int = round(population * (target_percent / 100))  # How many doses total to reach target percentage.
today: datetime = datetime.today()  # keep today date here
one_day: timedelta = timedelta(1)   # store a one day interval here
completion_date: datetime = datetime.today()    # store completion date here, initialize it to today.
doses_left: int = target_doses - doses_admin  # How many doses left to give.
days_left: int = 0  # holding place for number of days left

print("target_doses = " + str(target_doses))  # What's in the variable?
print("doses_left = " + str(doses_left))  # What's in the variable?

# Have to decide if we have already reached the target percentage or not.
# left my original calculation in comments.  Adding a day for the remainder is more precise than rounding.
if doses_left > 0:    # Have not reached the target yet, time to figure out when we will
    # days_left = doses_left // doses_per_day  # Calculate the number of whole days left to reach target
    # if 0 < doses_left % doses_per_day:  # is there a fraction of a day left after the division to account for?
    #     print("remainder from days_left = " + str(doses_left % doses_per_day))  # See what the remainder is.
    #     days_left = days_left + 1   # add one to the day counter for the fractional day needed.
    days_left = round(doses_left / doses_per_day)  # Alternate calculation, rounding is less precise.

    completion_date = today + (one_day * days_left)  # add the number of days left to today's date.

result1: str = "We will reach " + str(target_percent) + "% vaccination in " + str(days_left) + " days, "  # part 1
result2: str = "which falls on " + completion_date.strftime("%B %d, %Y") + "."  # part 2
print(result1 + result2)  # Had to break result string composition into two parts to fit in 119 characters
