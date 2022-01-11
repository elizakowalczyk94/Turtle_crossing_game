from turtle import Screen
import time
import car
import user_turtle
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = scoreboard.Scoreboard()
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
        scoreboard.level_up()
        user_turtle_obj.start_again()

    # detect collision with car
    if cars.detect_collision(user_turtle_obj):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
