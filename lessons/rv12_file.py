


























class Player:
    name: str = ""
    x: int
    y: int

    def __init__(self, n: str, a: int, b: int):
        self.name = n
        self.x = a
        self.y = b
    
    def __repr__(self) -> str:
        return f"{self.name} is at {self.x}, {self.y}."
    
    def move(self, dy: int) -> None:
        self.y += dy
    

def move(p: Player, dx: int) -> None:
    p.x += dx


def main() -> None:
    kaki: Player = Player("Kaki", 5, 7)
    kaki.move(2)
    move(kaki, -2)
    print(kaki)

main()