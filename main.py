from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

colors = ["DarkCyan", "coral3", "CadetBlue4", "LawnGreen", "OliveDrab3", "pink2", "tan1"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
