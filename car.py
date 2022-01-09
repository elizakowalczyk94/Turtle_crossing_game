from turtle import Turtle
import random

COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]

MOVE_DISTANCE = 20


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x_start = 300
        self.y_start = random.choice(range(-270, 270))
        self.goto(self.x_start, self.y_start)

    def move(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.y_start)
