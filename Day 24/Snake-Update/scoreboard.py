from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
DATAFILE = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    @staticmethod
    def read_high_score():
        with open(DATAFILE, mode="r") as file:
            high_score = int(file.read())
        return high_score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    def save_high_score(self):
        with open(DATAFILE, mode="w") as file:
            file.write(str(self.high_score))
