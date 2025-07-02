from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0 # create a high_score attribute so that when user play, and create a score, update it with current score, and game can't end until stop button pressed
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_score()

    # update the update_score() method, to display high score
    def update_score(self):
        self.clear()
        self.write(arg = f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg = "GAME OVER", align = ALIGNMENT, font = FONT)

    # reset() method is create for update high score, if current score > current high score, and set current score to 0
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_score()

    def increase_score(self):
        """

        :return:
        """
        self.score += 1
        self.update_score()