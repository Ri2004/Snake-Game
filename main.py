from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
# tracer method on screen object take a non-negative number, if 0 pass to this method, then tracer method turns off, tracer() turns on/off animation
# of turtle, animation means in this case is three pieces of turtles move separately when forward() is called on turtle, that's why call tracer() on
# screen object, to stop showing of movement of every piece of turtle, after all turtles are moved, then call update() on screen object, to show
# what is going on as output of the code, and after updating, again move turtles, and again call update() on screen object, and so on...
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food
    # distance() call on turtle object, and take a pair of numbers to compare turtle object with that pair, or it takes a turtle object as
    # argument, to compare turtle object which call distance() to the turtle object pass as argument. Here distance() compare snake.head
    # turtle object with food turtle object to check if snake and food distance is < 15 or not
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    # if snake head hit its own tail then game is over
    for segment in snake.segments[1:]:
        # if segment != snake.head and snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     score_board.game_over()
        
        # check with slicing, remove one extra check
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
