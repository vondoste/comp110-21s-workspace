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
#Declare and initialize our variables
population: int = 2 * int(input("Population: ")) #keep number of doses needed (2 doses per person) to fully vaccinate total population here.
doses_admin: int = int(input("Doses Administered: "))    #keep doses administered here
doses_per_day: int = int(input("Doses per day: "))   #keep doses per day here
target: int = int(input("Target percent vaccinated: "))  #keep target percentage here
today: datetime = datetime.today()  #keep today date here
one_day: timedelta = timedelta(1)   #store a one day interval here
completion_date: datetime = datetime.today()    #store completion date here, initialize it to today.
current_percentage: float = (doses_admin / population) * 100 # calculate current percentage vaccinated, store here
percent_left: float = target - current_percentage #calculate percentage left to go, negative number if already exceeded target,store here.
percent_per_day: float = (doses_per_day / population) * 100 #calculate percent per day and store here
days_left: int = 0  #holding place for number of days left


# Have to decide if we have already reached the target percentage or not.
if percent_left > 0:    #Have not reached the target yet, time to figure out when we will
    days_left = int(percent_left // percent_per_day) #Calculate the number of whole days left to reach target
    if 0 < percent_left % percent_per_day:  #is there a fraction of a day left after the division to account for?
        days_left = days_left + 1   #add one to the day counter for the fractional day needed.

    completion_date = today + (one_day * days_left)#add the number of days left to today's date.


print("We will reach " + str(target) + "% vaccination in " + str(days_left) + " days, which falls on " + completion_date.strftime("%B %d, %Y") + ".")
