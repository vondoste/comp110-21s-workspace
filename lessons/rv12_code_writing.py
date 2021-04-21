from typing import Union

class Account:
    balance: float

    def __init__(self, amnt: float):
        self.balance = amnt

    def __repr__(self) -> str:
        return f"Account with a balance of {self.balance}"
    
    def deposit(self, amnt: float) -> None:
        self.balance += amnt
    
    def withdraw(self, amnt: float) -> float:
        self.balance -= amnt
        return amnt
    
    
    
