"""Examples of list and loop algorithm."""

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned."""
    # 1. Initialize total and index 1 to 0
    total: int =0
    i: int = 0
    # 2. While index i is valid, meaning i < len(xs)
    while i < len(xs):
        #    2.True) take xs[i] and add it to total
        total += xs[i]
        #    2.True)  increase i by one, moving it to the next index
        i += 1

    # 2.False) result is stored in total variable
    return total


# Example usage of the sum_algo function
odds: list[int] = [1, 3, 5, 7]
odds_sum: int = sum_algo(odds)
print(odds_sum)