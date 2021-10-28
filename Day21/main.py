from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
import random
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Dectect Collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Dectect collision with Wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Dectect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # for seg_num in range(len(segments) - 1, 0, -1):

    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)

    # segments[0].forward(10)


screen.exitonclick()
