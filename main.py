from turtle import Screen
import time
import car
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")

screen.tracer(0)

car_list = []

cars = car.Car(10)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_all()

screen.exitonclick()
