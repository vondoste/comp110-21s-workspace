from typing import Union


def concat(lhs: list[str], rhs: Union[str, list[str]]) -> list[str]:
    xs: list[str] = []
    if isinstance(rhs, str):
        for item in lhs:
            xs.append(item + rhs)
    else:
        assert len(lhs) == len(rhs)
        for i in range(len(lhs)):
            xs.append(lhs[i] + rhs[i])
    return xs


first: list[str] = ["Kaki", "Kris"]
last: list[str] = ["Ryan", "Jordan"]
full: list[str] = concat(last, "/")
full = concat(full, first)
print(full)