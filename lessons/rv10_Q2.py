def main() -> None:  # QZ03 Q2
    april: list[bool] = [False, False, True]
    fools: list[bool] = [False, True, True]
    hehe: list[bool] = and_masks(april, fools)
    print(hehe)


def and_masks(lhs: list[bool], rhs: list[bool]) -> list[bool]:
    result: list[bool] = []
    i: int = 0
    while i < len(lhs):
        result.append(lhs[i] and rhs[i])
        i += 1
    return result


if __name__ == "__main__":
    main()