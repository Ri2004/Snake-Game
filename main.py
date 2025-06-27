from turtle import Screen
from snake import Snake
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



screen.exitonclick()
