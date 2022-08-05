import turtle
from turtle import Turtle, Screen, colormode
from random import choice

colors = [
    (224, 162, 65), (18, 43, 84), (238, 229, 220), (135, 61, 85), (227, 239, 233), (175, 61, 43), (126, 38, 60),
    (57, 48, 35), (21, 86, 61), (246, 196, 52), (18, 114, 143), (195, 140, 160), (228, 85, 39), (56, 139, 72),
    (229, 173, 190), (154, 188, 179), (194, 101, 133), (24, 64, 53), (58, 71, 38), (165, 204, 199), (68, 22, 42),
    (65, 155, 81), (34, 44, 103), (145, 165, 183), (204, 183, 33), (122, 41, 33), (5, 84, 112), (228, 175, 163)
]

screen = Screen()
timmy = Turtle()
timmy.penup()
timmy.speed(0)
colormode(255)
initial_x = -300
initial_y = -300
distance = 50
timmy.hideturtle()

for i in range(10):
    for j in range(10):
        color = choice(colors)
        timmy.setposition(initial_x + j * distance, initial_y + i * distance)
        timmy.dot(20, color)

screen.exitonclick()

