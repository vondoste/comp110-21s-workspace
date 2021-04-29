def fly(s: str, i: int) -> str:
    if i > len(s):
        return ""
    elif i == len(s) - 1:
        return s[i]
    else:
        item: str = s[i]
        print(item)
        rest: str = fly(s, i + 1)  # Avoids infinite recursion
        print(item)
        return item + rest + item


print(fly("abc", 0))
print(fly("hello world", 0))