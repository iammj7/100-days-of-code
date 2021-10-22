from turtle import Screen, Turtle, numinput
import random

tim = Turtle()
tom = Turtle()
colors = [
    "pale turquoise",
    "dark green",
    "misty rose",
    "deep sky blue",
    "maroon",
    "medium violet red" "green",
    "yellow",
]

# for _ in range(3):
#     tim.color("blue")
#     tim.right(360 / 3)
#     tim.forward(100)

# for _ in range(4):
#     tim.color("red")
#     tim.right(90)
#     tim.forward(100)

# for _ in range(5):
#     tim.color("yellow")
#     tim.right(360 / 5)
#     tim.forward(100)

# for _ in range(6):
#     tim.color("green")
#     tim.right(360 / 6)
#     tim.forward(100)

# for _ in range(7):
#     tim.color("red")
#     tim.right(360 / 7)
#     tim.forward(100)

# for _ in range(8):
#     tim.color("green")
#     tim.right(360 / 8)
#     tim.forward(100)


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tom.forward(100)
        tom.right(angle)


for shape_side_n in range(3, 11):
    tom.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
