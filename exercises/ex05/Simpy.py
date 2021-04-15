"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730366999"


class Simpy:
    """Simpy - a simple Numpy-like class for learning purposes."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, input: list[float]):
        """Constructor, takes list[float] creates a Simpy object with that value."""
        self.values = input
    
    def __repr__(self) -> str:
        """Builds a str representation of the object like Simpy(...), with the values inside the ()."""
        result: str = ""
        result += "Simpy(["
        for i in range(len(self.values)):
            if i == (len(self.values) - 1):
                result += f"{self.values[i]}])"
            else:
                result += f"{self.values[i]}, "
        return result
    
    def fill(self, value: float, count: int) -> None:
        """Fills a Simpy object with {count} copies of {value}."""
        assert count > 0
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
        """SimpyC[i] = SimpyA[i] + float or SimpyC[i] = SimpyA[i] + SimpyB[i]."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs)
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """SimpyC[i] = SimpyA[i] ** float or SimpyC[i] = SimpyA[i] ** SimpyB[i]."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs)
        return Simpy(result)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """SimpyC[i] = SimpyA[i] % float or SimpyC[i] = SimpyA[i] % SimpyB[i]."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs)
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """result[i] = True if SimpyA[i] == float or result[i] = True if SimpyA[i] == SimpyB[i]."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """result[i] = True if SimpyA[i] > float or result[i] = True if SimpyA[i] > SimpyB[i]."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        else:
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return float = SimpyA[rhs] or return SimpyB containing all SimpyA[i] where rhs[i] is True."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)