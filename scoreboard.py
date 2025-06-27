from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.write(arg = f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg = "GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        """

        :return:
        """
        self.score += 1
        self.clear()
        self.update_score()