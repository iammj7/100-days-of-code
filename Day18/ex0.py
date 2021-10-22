from turtle import Screen, Turtle, screensize

tim = Turtle()
tom = Turtle()


# for _ in range(4):
#    tim.forward(100)
#    tim.right(90)

# tom.shape("turtle")

for _ in range(50):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()


screen = Screen()
screen.exitonclick()
