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
today: datetime = datetime.today()  # keep today's date here
one_day: timedelta = timedelta(1)   # store a one day time interval here
completion_date: datetime = datetime.today()    # store completion date here, initialize it to today.
doses_left: int = target_doses - doses_admin  # How many doses left to give.
days_left: int = 0  # holding place for number of days left


# Have to decide if we have already reached the target percentage or not.
if doses_left > 0:    # Have not reached the target yet, time to figure out when we will
    days_left = round(doses_left / doses_per_day)  # calculate number of days needed, round it off to int.

    completion_date = today + (one_day * days_left)  # add the number of days left to today's date.

# Since we are limited to 119 characters for a line, composing answer into 2 different strings.
result1: str = "We will reach " + str(target_percent) + "% vaccination in " + str(days_left) + " days, "  # part 1
result2: str = "which falls on " + completion_date.strftime("%B %d, %Y") + "."  # part 2
print(result1 + result2)  # Concatenating the two halves of our result to display the final result.
