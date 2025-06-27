from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
# tracer method on screen object take a non-negative number, if 0 pass to this method, then tracer method turns off, tracer() turns on/off animation
# of turtle
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for position in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(starting_positions[position])
    segments.append(new_segment)


screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1,  0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(x=new_x, y=new_y)

    segments[0].forward(20)
    segments[0].left(90)



screen.exitonclick()
