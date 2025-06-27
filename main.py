from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
# tracer method on screen object take a non-negative number, if 0 pass to this method, then tracer method turns off, tracer() turns on/off animation
# of turtle
screen.tracer(0)
snake = Snake()


screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()
