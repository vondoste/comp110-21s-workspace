"""The insertion sort algorithm."""


def isort(xs: list[int]) -> None:
    i: int = 1
    j: int
    while i < len(xs):  # progresses through the list from 0 to the last position
        j = i
        while j > 0 and xs[j] < xs[j - 1]:  # this loop swaps incorrect items as far to the front as is needed.
            swap(xs, j, j-1)
            j -= 1

        i += 1


def swap(xs: list[int], i: int, j: int) -> None:  # swaps any two items the list.
    temp: int = xs[i]
    xs[i] = xs[j]
    xs[j] = temp


nums: list[int] = [2, 3, 1, 4, -1, 20, 10, 5, 2, 1]
isort(nums)
print(nums)