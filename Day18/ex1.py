# Draw a dashed line
from turtle import Turtle, Screen

tim = Turtle()

for i in range(15):
    tim.forward(10)  # moving turtle
    tim.penup()  # this will leave black white line
    tim.forward(10)  # blank forward
    tim.pendown()  # now pen down


screen = Screen()
screen.exitonclick()
