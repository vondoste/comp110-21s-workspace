"""Examples of built-in sorting facilities in Python."""

scores: list[int] = [95, 96, 80, 99, 78, 60]
sorted_scores: list[int] = sorted(scores)

print("Built-in sort function")
print(f"sorted_scores: {sorted_scores}")
print(f"scores: {scores}")

scores.sort()  # invokes the lists .sorted() method.  Sorts the original list with return of None
print(scores)