from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 280)
        self.color("white")
        self.hideturtle()
        self.level = 1
        self.write_on_screen()

    def write_on_screen(self, text="Level: 1"):
        self.write(arg=text,
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_on_screen(text=f"Level: {self.level}")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",
                   move=False,
                   align="center",
                   font=FONT)
