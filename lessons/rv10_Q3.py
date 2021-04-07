def zip_dict(ks: list[str], vs:list[str]) -> dict[str, str]:
    d: dict[str, str] = {}

    if len(ks) != len(vs):
        return d

    i: int = 0
    while i < len(ks):
        d[ks[i]] = vs[i]
        i += 1
    
    return d


a: list[str] = ["ROY", "UNC", "ROY", "UNC"]
b: list[str] = ["hi", "W", "bye", "L"]
c: dict[str, str] = zip_dict(a, b)
print(c)