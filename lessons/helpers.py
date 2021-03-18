"""Example functions that can be imported elsewhere."""


THE_ANSWER: int = 42

def shout(message: str) -> None:
    print(message.upper())

def whisper(message: str) -> None:
    print(message.lower())


print("helpers.py was evaluated")

if __name__ == "__main__":
    print("helpers.py was run as a module")
else:
    print(__name__)
    print("helpers.py was imported as a module")