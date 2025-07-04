from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # Create a separate variable because first segment always needed to set heading for movement of snake

    def create_snake(self):
        """
        Create Snake body by creating 3 Turtles
        :return:
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # reset() method is use to when snake hits on wall, or its own tail, then move the segments of snake body out of screen co-ordinate, and create new snake body
    # created at first time of starting game with 3 segments, and set head of snake to first segment
    def reset(self):
        for seg in self.segments:
            seg.goto(x = 1000, y = 1000)

        self.segments.clear() # clear the screen so no segment of snake is present
        self.create_snake()
        self.head = self.segments[0]  # Create a separate variable because first segment always needed to set heading for movement of snake

    def extend(self):
        """
        Add a new segment to the snake
        :return:
        """
        self.add_segment(self.segments[-1].position())


    def move(self):
        """
        Move snake forward, left, right, backward
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


