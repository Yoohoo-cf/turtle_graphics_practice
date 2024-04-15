# import colorgram
#
# colors = colorgram.extract("painting.jpeg", 10)
#
# rgb_colors = []
#
# for color in colors:
#     rgb_color = (color.rgb[0], color.rgb[1], color.rgb[2])
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("arrow")
tim.penup()
tim.hideturtle()
tim.speed("fastest")


colors = [(234, 241, 247), (247, 240, 245), (244, 249, 246), (141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()