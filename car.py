from turtle import Turtle
import random

COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray"]

MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_start = random.choice(range(-250, 250))
            new_car.goto(300, y_start)
            self.cars_list.append(new_car)

    def move_all(self):
        for car in self.cars_list:
            car.forward(MOVE_DISTANCE)

    def detect_collision(self, turtle):
        car_dist = []
        for elem in self.cars_list:
            car_dist.append(elem.distance(turtle))
        if any(car_dist) < 20:
            return False
        else:
            return True
