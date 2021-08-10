from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
FONT2 = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            content = int(file.read())
        self.highest_score = content
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def increase_highest_score(self):
        self.clear()
        with open("data.txt", "w") as file:
            file.write(str(self.score))
        self.update_scoreboard()

