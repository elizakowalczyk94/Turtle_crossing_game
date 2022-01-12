from turtle import Turtle

MOVE_DISTANCE = 10


class UserTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.shapesize(1, 1)
        self.setheading(90)
        self.start_again()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        self.goto(0, -280)
