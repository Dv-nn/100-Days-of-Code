from turtle import Turtle, Screen
from time import sleep

tim = Turtle()
screen = Screen()
    
def moove_forwards():
    tim.forward(10)  
def move_backwards():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10    
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10    
    tim.setheading(new_heading)



screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_forwards, "s")
clear()
screen.onkey(turn_left, "a")
screen.onkey(turn_rigth, "d")

screen.exitonclick()



