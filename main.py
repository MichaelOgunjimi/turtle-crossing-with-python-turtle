import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Initialize the player, car and scoreboard objects
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Move the player on the screen
screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create a car object and move it
    cars.create_car()
    cars.move_cars()

    #Detect when the play as successfully crossed
    if player.is_at_finish_line():
        player.refresh()
        cars.level_up()
        scoreboard.update()

    #Detect when the player collides with a car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()