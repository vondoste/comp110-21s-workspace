
square_to_root: dict[int, int] = {}

i: int = 1
while i < 5:
    square_to_root[i ** 2] = i
    i += 1

print(square_to_root)


"""Diagram 1"""
a: dict[str, int] = {"k": 1}  # dict literal, creates a new dict on the heap.
b: dict[str, int] = a  # refers to existing dict on the heap
c: dict[str, int] = b  # refers to existing dict on the heap
a["k"] = 2  # changes value of "k" in existing dictionary.
b = {"k": 3}  # dict literal, creates a new dict on the heap, assigns b to point to it.
print(a["k"])
print(b["k"])
print(c["k"])

def invert(kvs: dict[str, int]) -> dict[int, str]:
    result: dict[int, str] = {}
    for key in kvs:
        result[kvs[key]] = key
    return result


counts: dict[str, int] = {"a": 1, "b": 2, "c": 1}
print(len(counts))

freqs: dict[int, str] =  invert(counts)
print(freqs[1])
print(len(freqs))


"""Diagram 3"""
# practice problems

"""Diagram 4"""
# practice problems
def add(xs: list[int]) -> int:
    if len(xs) == 0:
        return 0
    
    else:
        x: int = xs.pop[]
        y = add(xs)
        return x + y

nums: list[int]