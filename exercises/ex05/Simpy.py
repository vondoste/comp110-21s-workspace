"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730366999"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, input: list[float]):
        """Constructor, takes list[float] creates a Simpy object with that value."""
        self.values = input
    
    def __repr__(self) -> str:
        """Builds a str representation of the object like Simpy(...), with the values inside the ()."""
        result: str = ""
        result += "Simpy("
        for i in range(len(self.values)):
            if i == (len(self.values) - 1):
                result += f"{self.values[i]})"
            else:
                result += f"{self.values[i]}, "
        return result
    
    def fill(self, value: float, count: int) -> None:
        """Fills a Simpy object with {count} copies of {value}."""
        self.values = []
        for i in range(count):
            self.values.append(value)
        return
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills a Simpy object with values [start, stop), or (stop, start]  in {step} increments."""
        assert step != 0.0
        if step > 0:
            assert start < stop
        else:
            assert start > stop
        self.values = []
        holding: float = start
        if step > 0:
            while holding < stop:
                self.values.append(holding)
                holding += step
        else:
            while holding > stop:
                self.values.append(holding)
                holding += step
        return
    
    def sum(self) -> float:
        """Returns the sum of the numbers in self.values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        
