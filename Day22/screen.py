from turtle import Turtle, Screen


paddle_1 = Turtle("square")
paddle_1.color("white")
paddle_1.shapesize()

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)


screen.exitonclick()
