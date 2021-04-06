"""Examples of object oriented programming concepts."""

class Point:
    # Defining attributes (related variables)
    # of out class.  Set attributes to initial values.
    x: float
    y: float

    def __init__(self, x: float, y: float):  # __init__ is a custom constructor, initializes new object.
        """Construct a point by giving x and y args."""
        self.x = x
        self.y = y
        # pretend that "return self" is the last line of the constructor.  The self reference and the Point
        # type are handled automagically.  A constructor only has one purpose, create a new object, and 
        # return the reference.

    def __repr__(self) -> list:
        """Magic method to represent object as str."""
        return f"{self.x}. {self.y}"

    def invert(self) -> None:
        """Swap x and y."""
        temp: float = self.x
        self.x = self.y
        self.y = temp


a: Point = Point(4.0, 5.0)  # Point() is constructor, constructs a new Point type object on heap pointed to by a
print(a.__repr__())
a.invert()
print(a.x)
print(a.y)

b: Point = Point(0.0, 0.0)  # Lines below assign to the objects attributes.
b.x = 2.0
b.y = -1.0
print(b)  # automatically calls __repr__ if it is defined.
