from turtle import Turtle, done

em: Turtle = Turtle()
i: int = 0
while i < 100:
    em.forward(2 * i)
    em.left(90)
    i += 1


done()
