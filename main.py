from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("arrow")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Make a Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + size_of_gap)


# tim.pensize(6)
tim.speed("fastest")
draw_spirograph(5)


screen.exitonclick()
