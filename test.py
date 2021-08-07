from turtle import Turtle, Screen


def up():
    for turtle in turtles:
        turtle.setheading(90)


def down():
    for turtle in turtles:
        turtle.setheading(270)


def left():
    for turtle in turtles:
        turtle.setheading(180)


def right():
    for turtle in turtles:
        turtle.setheading(0)

screen = Screen()
screen.setup(600,600) # makes the siz of the game
screen.bgcolor("coral")
screen.title("Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = list()
for position in positions:
    my_turtle = Turtle()
    my_turtle.penup()
    my_turtle.shape("square")
    my_turtle.turtlesize(0.8, 2, 2)
    my_turtle.goto(position)
    turtles.append(my_turtle)

screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
is_game_on = True
while is_game_on:
    for turtle in turtles:
        turtle.forward(20)


screen.exitonclick()
