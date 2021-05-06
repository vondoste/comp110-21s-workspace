from turtle import Turtle, done


TRUNK = 100.0
UP = 90.0

t: Turtle = Turtle()


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, UP)
    t.getscreen().update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3:
        ... # Base case: do nothing
    else:
        # Recursive case: Branch again
        # branch(length * 0.3, angle)
        branch(length * 0.56, angle + 35)
        branch(length * 0.9, angle - 30)
    # Bring the turtle back to it's starting point
    t.setheading(angle + 180.0)
    t.forward(length)


if __name__ == "__main__":
    t.speed(3)
    t.getscreen().tracer(0, 0)
    t.getscreen().onclick(tree)
    done()