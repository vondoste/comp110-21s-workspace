"""Given the main() and had to write the rest based on deduction."""








class Possum:
    is_smiling: bool = False
    age: int = 0
    name: str = ""

    def __init__(self, a: int, s: str):
        self.age = a
        self.name = s
        



















def main() -> None:
    mr: Possum = Possum(6, "Mr. Possum")
    mr.is_smiling = True