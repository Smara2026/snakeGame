import time
from turtle import *
import random

user_input = "y"
screen = Screen()
while user_input == "y":

    screen.colormode(255)
    screen.bgcolor("black")
    screen.title("SNAKE GAME")
    screen.setup(height=600, width=600)
    turtle_position = [(0, 0), (-20, 0), (-40, 0)]
    turtle_list = []
    screen.tracer(0)
    # food
    food = Turtle("circle")
    food.resizemode("user")
    food.shapesize(.8, .8, .8)
    # food.ht()
    food.color("white")
    food.up()
    scoreboard = Turtle()
    scoreboard.ht()
    scoreboard.up()
    scoreboard.color("white")
    scoreboard.goto(0, 275)
    score = 0
    scoreboard.write(arg=f"Score:{score}", align="center", font=('Arial', 15, 'normal'))
    gameover = Turtle()
    gameover.up()
    gameover.ht()
    gameover.color("white")
    gameover.goto(0, 150)


    def turn_left():
        if turtle_list[0].heading() == 90:
            turtle_list[0].left(90)
        elif turtle_list[0].heading() == 270:
            turtle_list[0].right(90)
        else:
            turtle_list[0].left(90)


    def turn_right():
        if turtle_list[0].heading() == 90:
            turtle_list[0].right(90)
        elif turtle_list[0].heading() == 270:
            turtle_list[0].left(90)
        else:
            turtle_list[0].right(90)


    def up():
        turtle_list[0].setheading(90)


    def down():
        turtle_list[0].setheading(270)


    # starting snake

    for position in turtle_position:
        new_turtle = Turtle(shape="square")
        new_turtle.up()
        new_turtle.color("white")
        new_turtle.speed("fastest")
        new_turtle.goto(position)
        turtle_list.append(new_turtle)
    # food

    food.goto(x=random.randint(-290, 290), y=random.randint(-290, 290))
    

    game_is_on = True
    while game_is_on:

        screen.listen()
        screen.onkey(fun=turn_left, key="Left")
        screen.onkey(fun=up, key="Up")
        screen.onkey(fun=turn_right, key="Right")
        screen.onkey(fun=down, key="Down")
        # moving the snake

        for turtle_index in range(len(turtle_list) - 1, 0, -1):
             turtle_list[turtle_index].goto(x=turtle_list[turtle_index - 1].xcor(),
                                           y=turtle_list[turtle_index - 1].ycor())
        turtle_list[0].fd(10)

        # eating food and adding a turtle

        if turtle_list[0].distance(food) < 15:
            score += 1
            scoreboard.clear()
            scoreboard.write(arg=f"Score:{score}", align="center", font=('Arial', 15, 'normal'))
            food.goto(x=random.randint(-290, 290), y=random.randint(-290, 290))
            new_turtle1 = Turtle("square")
            new_turtle2 = Turtle("square")
            new_turtle1.color("white")
            new_turtle2.color("white")
            new_turtle1.up()
            new_turtle2.up()
            new_turtle1.goto(turtle_list[len(turtle_list) - 1].xcor(), turtle_list[len(turtle_list) - 1].ycor())
            new_turtle2.goto(turtle_list[len(turtle_list) - 1].xcor(), turtle_list[len(turtle_list) - 1].ycor())
            turtle_list.append(new_turtle1)
            turtle_list.append(new_turtle2)

        screen.update()
        for turtles_index in range(2, len(turtle_list)):
            if abs(turtle_list[0].xcor() - turtle_list[turtles_index].xcor()) < 10 and abs(
                    turtle_list[0].ycor() - turtle_list[turtles_index].ycor()) < 10:
                game_is_on = False
                gameover.write(arg="GAME OVER", align="center", font=('Ariel', 15, 'normal'))
                user_input = screen.textinput("Restart??", "Press y to restart and n to leave")
                break
        if (turtle_list[0].xcor() > 290 or turtle_list[0].xcor() < -290 or turtle_list[0].ycor() > 290 or
                turtle_list[0].ycor() < -290):
            gameover.write(arg="GAME OVER", align="center", font=('Ariel', 15, 'normal'))
            user_input = screen.textinput("Restart??", "Press y to restart and n to leave")
            break
        time.sleep(0.05)
    screen.clearscreen()
screen.bye()
