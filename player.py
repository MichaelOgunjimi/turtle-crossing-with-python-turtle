STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        self.shape("turtle")
        self.penup()
        self.setheading(UP)
        self.refresh()

    def refresh(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() == self.finish_line:
            return True
        else:
            return False

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
