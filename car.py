import time
from turtle import Turtle
import random

COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]

MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self, car_no=10):
        super().__init__()
        self.car_no = car_no
        self.cars_list = []
        for _ in range(self.car_no):
            self.create_cars()

    def create_cars(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.x_start = random.choice(range(300, 900))
        new_car.y_start = random.choice(range(-270, 270))
        new_car.goto(new_car.x_start, new_car.y_start)
        self.cars_list.append(new_car)

    def move_all(self):
        for car in self.cars_list:
            if car.xcor() < -300:
                new_y = random.choice(range(-270, 270))
                car.goto(300, new_y)
            else:
                car.forward(MOVE_DISTANCE)
