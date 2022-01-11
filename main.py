from turtle import Screen
import time
import car
import user_turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")

screen.tracer(0)

car_list = []

cars = car.Car()
user_turtle_obj = user_turtle.UserTurtle()

screen.listen()
screen.onkey(user_turtle_obj.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_all()

    # detect score
    if user_turtle_obj.ycor() > 280:
        print("score")

screen.exitonclick()
