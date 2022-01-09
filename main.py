from turtle import Screen
import time
import car

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")

screen.tracer(0)
car = car.Car()

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()

    car.move()

screen.exitonclick()
