"""Examples using loops."""

count: int = 0
while input("Do you need more love? yes/no - ") == "yes":
    # Body block of the while loop is evaluated
    # when the test expression is true
    print("I love you!")
    count += 1
    print(f"Count is {count} ")

# Iterating a specific number of times
i: int = 0  # A classic traditional variable used for index
iterations: int = 1000000

while i < iterations:
    if i % 1000 == 0:
        print(f"I love you! i: {i}")
    i += 1  # incrementing or decrementing the index MUST happen inside the loop, or it's an infinite loop.
            # also, it must move closer to the while condition becoming false.

print("Have a lovely day.")