import turtle

wn = turtle.Screen()
wn.title("Pong Game v1.0")
wn.setup(800,600)
wn.bgcolor("black")
wn.tracer(0)

# set score = 0 at the beginning
score = 0

# Paddle is controlled by left/right key strokes
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("limegreen")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0,-250)

# Ball is program controlled
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25 # speed in X direction
ball.dy = 0.25 # speed in Y direction

# Show score on top of the window
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
pen.pendown()
          
def goLeft():
      x = paddle.xcor()
      x -= 50
      paddle.setx(x)
def goRight():
      x = paddle.xcor()
      x += 50
      paddle.setx(x)

wn.listen()
wn.onkeypress(goLeft, "Left")
wn.onkeypress(goRight, "Right")

# Game Loop
while True:
      wn.update()

      # Move Ball
      ball.setx(ball.xcor() + ball.dx)
      ball.sety(ball.ycor() + ball.dy)

      # Detect Top and Bottom Walls
      if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  #changes the direction of movement
      elif ball.ycor() < -290:
            score -= 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            ball.sety(-290)
            ball.dy *= -1  #changes the direction of movement

      # Left and Right wall reflection
      if ball.xcor() > 390:  # right wall
            ball.dx *= -1
      elif ball.xcor() < -390:  #left wall
            ball.dx *= -1

      # Paddle detection and reflection
      if ball.ycor() < -230 and \
         ball.xcor() < paddle.xcor() + 50 and \
         ball.xcor() > paddle.xcor() - 50:
            score += 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            ball.sety(-220)
            ball.dy *= -1
