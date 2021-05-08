class Cat:
    name: str = "boots"

    def speak(self) -> None:
        print(f"meow")


class Dog:
    name: str

    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> None:
        print(f"woof")


def main() -> None:
    ada: Cat = Cat()
    boots: Dog = Dog("ada")
    nelli: Dog = boots
    scout: Cat = ada
    nelli.speak()
    scout.speak()


if __name__ == "__main__":
    main()