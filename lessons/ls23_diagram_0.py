class Dog:
    name: str

    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return f"{self.name}: woof"


class Cat:
    name: str

    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return f"{self.name}: meow"


fido: Cat = Cat("Cleo")
leo: Dog = Dog("Loki")

print(fido.speak())
print(leo.speak())