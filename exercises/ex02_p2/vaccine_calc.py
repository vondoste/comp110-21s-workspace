"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730366999"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_left: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    completion_date: str = future_date(days_left)
    # TODO 5: Print the expected output using the variables above.
    result1: str = "We will reach " + str(target) + "% vaccination in " + str(days_left) + " days, "  # part 1
    result2: str = "which falls on " + completion_date + "."  # part 2
    print(result1 + result2)  # Concatenating the two halves of our result to display the final result.


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculates number of days needed to reach target percentage of population."""
    target_doses: int = round((2 * population) * (target / 100))  # 2 doses/person * population * target / 100.
    doses_left: int = target_doses - doses  # Store remaining number of doses here.
    days_left = round(doses_left / doses_per_day)  # calculate number of days needed, round it off to int.
    return days_left


# TODO 3: Define future_date function
def future_date(days: int) -> str:
    """Calculates the date of x days in the future, based on todays date."""
    today: datetime = datetime.today()  # keep today's date here
    one_day: timedelta = timedelta(1)   # store a one day time interval here
    date: datetime = today + (one_day * days)  # add the number of days left to today's date.
    result: str = str(date.strftime("%B %d, %Y"))
    return result


if __name__ == "__main__":
    main()
