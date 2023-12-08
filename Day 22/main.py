from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
scren.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto()

def go_up():
  new_y = paddle.ycor() + 20
  paddle.goto(paddle.xcor(), new_y)

def go_down():
  new_y = paddle.ycor() - 20
  paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_one = True
while game_is_one:
  screen.update()

screen.exitonclick(350, 0)




