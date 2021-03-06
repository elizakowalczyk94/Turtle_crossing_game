from turtle import Turtle
import random

COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
          "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray"]

MOVE_INCREMENT = 2


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.move_distance = 5
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
            car.forward(self.move_distance)

    def detect_collision(self, player):
        cars_dist = []
        for car in self.cars_list:
            cars_dist.append(car.distance(player))
        return list(filter(lambda x: x < 20, cars_dist))

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
