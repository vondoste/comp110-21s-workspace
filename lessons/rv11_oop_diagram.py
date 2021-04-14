"""From rv11"""
from __future__ import annotations


class Account:
    balance: float

    def __init__(self, amnt: float):
        self.balance = amnt
    
    def deposit(self, amnt: float) -> None:
        self.balance += amnt
    
    def withdraw(self, amnt: float) -> float:
        self.balance -= amnt
        return amnt

    def transfer(self, amnt: float, to: Account) -> None:
        self.deposit(to.withdraw(amnt))
    
    def __add__(self, other: Union [float, Account]) -> Account:
        result: Account
        if isinstance(other, float):
            result = Account(self.balance + other)
        else:
            result = Account(self.balance + other.balance)
        return result


alice: Account = Account(100.0)
bob: Account = Account(50.0)
alice.transfer(25.0, bob)
print(alice.balance)
print(bob.balance)

both: Account = alice + bob
print(both.balance)
both = alice + 70.0
print(both.balance)