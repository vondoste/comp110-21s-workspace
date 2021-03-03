"""EX03 - prime functions."""

__author__: str = "730366999"

from typing import List

def is_prime(x: int) -> bool:
    """
    The Prime Detective, x must be greater than 1.
    
    We know that a prime number is divisible by itself and by 1.
    It should not be evenly divisible by anything else.
    We will loop through every value from x-1 down to 2, looking for 
    a number that evenly divides x.
    If none do, then return True
    """
    i: int = x - 1  # set i = to x -1 

    #  print(f"running is_prime on {x} ")

    if not(x > 1):
        return False

    while i > 1:
        if 0 == (x % i):  # if x is evenly divisible by i, then can't be a prime number
            return False
        i -= 1

    return True


def list_primes(lower: int, upper: int) -> list[int]:
    """Returns a list of prime numbers from lower <= x < upper."""
    list_of_primes: List[int] = []  # Initialize a list to store primes in.
    i: int = lower  # Initialize i to value of lower.
    
    # print(f"lower: {lower} ")
    # print(f"upper: {upper} ")
    # print(f"i: {i} ")
    # print(f"list_of_primes: {list_of_primes} ")

    while i < upper:  # Check every value lower <= i < upper
        if is_prime(i):
            list_of_primes.append(i)
            # print(f"list_of_primes = {list_of_primes} ")
        
        i += 1
    
    return list_of_primes


def main() -> None:
    """Entrypoint of the program."""
    print(f"2 is prime? {is_prime(2)}")
    print(f"3 is prime? {is_prime(3)}")
    print(f"4 is prime? {is_prime(4)}")
    print(f"5 is prime? {is_prime(5)}")
    print(f"6 is prime? {is_prime(6)}")
    print(f"7 is prime? {is_prime(7)}")
    print(f"Prime numbers on the range of [1,10): {list_primes(1,10)} ")
    print(f"Prime numbers on the range of [11,100): {list_primes(11,100)} ")


if __name__ == "__main__":
    main()