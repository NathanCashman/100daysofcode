from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        self.setposition(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.setposition(self.xcor(), self.ycor() - MOVE_DISTANCE)
