from turtle import Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for _ in range(4):
  timmy_the_turtle.forward(100)
  timmy_the_turtle.rigth(90)
  timmy_the_turtle.penup()
  timmy_the_turtle.rigth(30)
  timmy_the_turtle.pendown()

# -------------------------------------------
import Turtle as t

tim = t.Turtle()

def draw_shape():
  for _ in range(num_sides):
    angle = 360 / num_sides
    tim.forward(100)
    tim.rigth(angle)

for shape_side_n in range(3, 11):
  draw_shape(shape_side_n)



