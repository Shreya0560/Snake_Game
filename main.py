from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Shreya's Amazing Snake Game :)")
screen.tracer(0)
game_on = True

#Creating a Snake and Food object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    # refreshes screen after a delay of 0.1 seconds
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.set_location()
        scoreboard.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_on = False
        #scoreboard.game_over()
        scoreboard.reset()

    # #Detect collision with its own body
    # for square in snake.squares:
    #     if square == snake.head:
    #         pass
    #     elif snake.head.distance(square) < 10:
    #         game_on = False
    #         scoreboard.game_over()

    # #Detect collision with its own body
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            #game_on = False
            #scoreboard.game_over()
            scoreboard.reset()




screen.exitonclick()